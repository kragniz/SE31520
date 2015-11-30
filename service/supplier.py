#!/usr/bin/env python

import argparse
import hashlib
import json

from flask import Flask, jsonify
import yaml

app = Flask(__name__)

wines = []

@app.route('/api/wines/<string:wine_id>', methods=['GET'])
def get_wine(wine_id):
    for wine in wines:
        if wine.get('id') == wine_id:
            return jsonify({'wine': wine})

@app.route('/api/wines', methods=['GET'])
def get_wines():
    return jsonify({
        'wines': [
            {wine.get('id'): wine.get('name')} for wine in wines
        ]
    })

@app.route('/api', methods=['GET'])
def index():
    return jsonify({'user': 'anon'})

def get_hash(d):
    '''Return a deterministic hash of a dictionary'''
    hash_object = hashlib.sha1(json.dumps(d))
    return hash_object.hexdigest()

def get_args():
    '''Parse command line arguments'''
    parser = argparse.ArgumentParser()
    parser.add_argument('wines', help='wine yaml file')
    return parser.parse_args()

def get_wine_data(filename):
    '''Return a dict containing data loaded from config file'''
    with open(filename) as f:
        y = yaml.load(f)

    return y.get('wines', [])

def main():
    args = get_args()
    wines_data = get_wine_data(args.wines)

    for wine in wines_data:
        sha1 = get_hash(wine)
        wine['id'] = sha1[0:16]
        wines.append(wine)

    app.run(host='0.0.0.0',
            port=8080,
            debug=True)

if __name__ == '__main__':
    main()
