#!/usr/bin/python3
"""Consumir y procesar datos de una API con Python"""

import requests


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post['title'])
    else:
        print(f"Error en la peticion: {response.status_code}")
