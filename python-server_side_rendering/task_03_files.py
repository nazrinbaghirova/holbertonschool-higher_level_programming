#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json():
    """Read products from JSON file"""
    with open('products.json', 'r') as file:
        return json.load(file)


def read_csv():
    """Read products from CSV file"""
    products = []

    with open('products.csv', 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)

    return products


@app.route('/products')
def products():

    source = request.args.get('source')
    product_id = request.args.get('id')

    # Check source
    if source not in ['json', 'csv']:
        return render_template(
            'product_display.html',
            error="Wrong source"
        )

    # Read data
    if source == 'json':
        products = read_json()
    else:
        products = read_csv()

    # Filter by id if provided
    if product_id:
        found_product = None

        for product in products:
            if str(product['id']) == str(product_id):
                found_product = product
                break

        if found_product is None:
            return render_template(
                'product_display.html',
                error="Product not found"
            )

        products = [found_product]

    return render_template(
        'product_display.html',
        products=products
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
