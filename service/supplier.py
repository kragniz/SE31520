#!/usr/bin/env python

import argparse
import hashlib
import json

from flask import Flask, jsonify
import yaml

app = Flask(__name__)

wines = []

@app.route('/wines', methods=['GET'])
def get_wines():
    return jsonify({'wines': [wine.get('id') for wine in wines]})

@app.route('/', methods=['GET'])
def index():
    return jsonify({'user': 'anon'})

def get_hash(d):
    hash_object = hashlib.sha1(json.dumps(d))
    return hash_object.hexdigest()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('wines', help='wine yaml file')
    args = parser.parse_args()

    with open(args.wines) as f:
        y = yaml.load(f)

    wines_data = y.get('wines', [])
    for wine in wines_data:
        sha1 = get_hash(wine)
        wine['id'] = sha1[0:16]
        wines.append(wine)

    app.run(host='0.0.0.0',
            debug=True)

if __name__ == '__main__':
    main()
