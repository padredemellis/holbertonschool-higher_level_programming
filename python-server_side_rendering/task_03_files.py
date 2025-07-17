from flask import Flask, render_template, request
import json
import csv
import os
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Funciones de lectura de datos
def read_json_products(file_path):
    """Lee y parsea productos desde un archivo JSON."""
    if not os.path.exists(file_path):
        logging.error(f"JSON file not found: {file_path}")
        return None
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON from {file_path}: {e}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error reading JSON file {file_path}: {e}")
        return None

def read_csv_products(file_path):
    """Lee y parsear productos desde un archivo CSV."""
    if not os.path.exists(file_path):
        logging.error(f"CSV file not found: {file_path}")
        return None
    products = [] # ¡CORREGIDO AQUÍ!
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # csv.DictReader lee cada fila como un diccionario usando los encabezados como claves
            reader = csv.DictReader(f)
            for row in reader:
                # Convertir 'id' y 'price' a tipos numéricos
                try:
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                    products.append(row)
                except ValueError as ve:
                    logging.warning(f"Skipping row due to data type error: {row} - {ve}")
                    continue
        return products
    except Exception as e:
        logging.error(f"Error reading CSV file {file_path}: {e}")
        return None

# Rutas existentes de la Tarea 1 y 2
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    items_list = []
    json_file_path = 'items.json'
    if not os.path.exists(json_file_path):
        return render_template('items.html', items=[], error_message="No se pudo cargar la lista de ítems.") # ¡CORREGIDO AQUÍ!
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            items_list = data.get('items', [])
    except json.JSONDecodeError as e:
        return render_template('items.html', items=[], error_message=f"Error al decodificar JSON: {e}") # ¡CORREGIDO AQUÍ!
    return render_template('items.html', items=items_list)

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    data = None
    error_message = None

    if source == 'json':
        data = read_json_products('products.json')
    elif source == 'csv':
        data = read_csv_products('products.csv')
    else:
        error_message = "Wrong source. Please specify 'json' or 'csv'."
        return render_template('product_display.html', error=error_message)

    if data is None:
        error_message = f"Error al cargar los datos desde la fuente: {source}."
        return render_template('product_display.html', error=error_message)

    if product_id:
        try:
            product_id = int(product_id)
            filtered_products = [p for p in data if p.get('id') == product_id]
            if not filtered_products:
                error_message = f"Product with ID {product_id} not found."
                return render_template('product_display.html', error=error_message)
            data = filtered_products
        except ValueError:
            error_message = "Invalid product ID. Must be an integer."
            return render_template('product_display.html', error=error_message)

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)