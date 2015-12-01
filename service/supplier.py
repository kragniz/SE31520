#!/usr/bin/env python

import argparse
import hashlib
import json

from flask import Flask, jsonify, abort
import yaml

app = Flask(__name__)

wines = []
supplier_name = ''

@app.route('/api/wines/<string:wine_id>', methods=['GET'])
def get_wine(wine_id):
    for wine in wines:
        if wine.get('id') == wine_id:
            return jsonify({'wine': wine})
    abort(404)

@app.route('/api/wines/', methods=['GET'])
def get_wines():
    return jsonify({
        'wines': [
            {wine.get('id'): wine.get('name')} for wine in wines
        ]
    })

@app.route('/api/', methods=['GET'])
def index():
    return jsonify({'supplier': supplier_name,
                    'user': 'anon'})

def get_hash(d):
    '''Return a deterministic hash of a dictionary'''
    hash_object = hashlib.sha1(json.dumps(d))
    return hash_object.hexdigest()

def get_args():
    '''Parse command line arguments'''
    parser = argparse.ArgumentParser()
    parser.add_argument('wines', help='wine yaml file')
    return parser.parse_args()

def get_wine_data(raw_wine_data):
    '''Return a dict containing data loaded from config file'''
    return raw_wine_data.get('wines', [])

def get_wine_supplier(raw_wine_data):
    '''Return a string containing the supplier name set in the config file'''
    return raw_wine_data.get('supplier', 'No supplier name set')

def main():
    args = get_args()

    with open(args.wines) as f:
        raw_wine_data = yaml.load(f)

    wines_data = get_wine_data(raw_wine_data)

    global supplier_name
    supplier_name = get_wine_supplier(raw_wine_data)

    for wine in wines_data:
        sha1 = get_hash(wine)
        wine['id'] = sha1[0:16]
        wines.append(wine)

    app.run(host='0.0.0.0',
            port=8080,
            debug=True)

if __name__ == '__main__':
    main()
