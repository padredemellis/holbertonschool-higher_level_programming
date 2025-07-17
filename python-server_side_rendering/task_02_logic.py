#!/usr/bin/python3
from flask import Flask, render_template
import json
import os
import logging  # Importación esencial

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
    # Usar ruta absoluta para el JSON
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(base_dir, 'items.json')
    
    if not os.path.exists(json_file_path):
        logging.error(f"File not found: {json_file_path}")
        return render_template('items.html', 
                               items=[], 
                               error_message="Items list unavailable")

    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            items_list = data.get('items', [])
    except json.JSONDecodeError as e:
        logging.error(f"JSON error: {e}")
        return render_template('items.html', 
                               items=[], 
                               error_message="Invalid items data")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return render_template('items.html', 
                               items=[], 
                               error_message="Loading error")

    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)