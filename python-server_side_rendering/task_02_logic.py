#!/usr/bin/python3
from flask import Flask, render_template
import json
import os
import logging  # Importación faltante

app = Flask(__name__)

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
    json_file_path = 'items.json'
    
    if not os.path.exists(json_file_path):
        logging.error(f"Error: file {json_file_path} not found")
        return render_template('items.html', 
                               items=[], 
                               error_message="The list of items could not be loaded.")
    
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            items_list = data.get('items', [])  # Valor por defecto corregido
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON from {json_file_path}: {e}")
        return render_template('items.html', 
                               items=[], 
                               error_message="Error reading item data.")
    except Exception as e:
        logging.error(f"Unexpected error reading {json_file_path}: {e}")
        return render_template('items.html', 
                               items=[], 
                               error_message="Unexpected error loading items.")

    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
