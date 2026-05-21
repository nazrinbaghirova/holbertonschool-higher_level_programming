#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json():
    with open('products.json', 'r') as file:
        return json.load(file)


def read_csv():
    products = []

    with open('products.csv', 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)

    return products


def read_sql():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Products")
    rows = cursor.fetchall()

    conn.close()

    products = []

    for row in rows:
        products.append({
            'id': row['id'],
            'name': row['name'],
            'category': row['category'],
            'price': row['price']
        })

    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    try:
        if source == 'json':
            data = read_json()

        elif source == 'csv':
            data = read_csv()

        elif source == 'sql':
            data = read_sql()

        else:
            return render_template(
                'product_display.html',
                error="Wrong source"
            )

        if product_id:
            product = []

            for item in data:
                if str(item['id']) == str(product_id):
                    product.append(item)

            if not product:
                return render_template(
                    'product_display.html',
                    error="Product not found"
                )

            data = product

        return render_template(
            'product_display.html',
            products=data
        )

    except Exception:
        return render_template(
            'product_display.html',
            error="Database error"
        )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
