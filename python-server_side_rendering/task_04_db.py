from flask import Flask, render_template, request, g
import json
import csv
import sqlite3
import os
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

DATABASE = 'products.db'

# Función para obtener la conexión a la base de datos
def get_db():
    """Establece y devuelve una conexión a la base de datos SQLite."""
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

# Función para cerrar la conexión a la base de datos
@app.teardown_appcontext
def close_connection(exception):
    """Cierra la conexión a la base de datos si está abierta."""
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
        logging.info("Database connection closed.")

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
    """Lee y parsea productos desde un archivo CSV."""
    if not os.path.exists(file_path):
        logging.error(f"CSV file not found: {file_path}")
        return None
    products = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
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

def read_sql_products(product_id=None):
    """Lee productos desde la base de datos SQLite."""
    try:
        db = get_db()
        cursor = db.cursor()
        if product_id:
            cursor.execute("SELECT id, name, category, price FROM Products WHERE id = ?", (product_id,))
        else:
            cursor.execute("SELECT id, name, category, price FROM Products")
        
        # Convertir filas a diccionarios
        products = [dict(row) for row in cursor.fetchall()]
        return products
    except sqlite3.Error as e:
        logging.error(f"SQLite database error: {e}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error reading from SQLite database: {e}")
        return None

# Rutas básicas
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
        return render_template('items.html', items=[], error_message="No se pudo cargar la lista de ítems.")
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            items_list = data.get('items', [])
    except json.JSONDecodeError as e:
        return render_template('items.html', items=[], error_message=f"Error al decodificar JSON: {e}")
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
    elif source == 'sql':
        # Convertir product_id a int si existe
        if product_id:
            try:
                product_id = int(product_id)
            except ValueError:
                error_message = "Invalid product ID. Must be an integer."
                return render_template('product_display.html', error=error_message)
        data = read_sql_products(product_id)
    else:
        error_message = "Wrong source. Please specify 'json', 'csv', or 'sql'."
        return render_template('product_display.html', error=error_message)

    if data is None:
        error_message = f"Error loading data from source: {source}."
        return render_template('product_display.html', error=error_message)

    # Filtrar por ID para fuentes no SQL
    if product_id and source != 'sql':
        try:
            product_id = int(product_id)
            filtered_products = [p for p in data if p.get('id') == product_id]
            if not filtered_products:
                error_message = "Product not found"
                return render_template('product_display.html', error=error_message)
            data = filtered_products
        except ValueError:
            error_message = "Invalid product ID. Must be an integer."
            return render_template('product_display.html', error=error_message)

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)