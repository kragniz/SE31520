#!/usr/bin/env python

import argparse

from flask import Flask, jsonify
import yaml

app = Flask(__name__)

wines = []

@app.route('/', methods=['GET'])
def index():
    return jsonify({'user': 'anon'})

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('wines', help='wine yaml file')
    args = parser.parse_args()

    with open(args.wines) as f:
        y = yaml.load(f)

    wines = y.get('wines', [])

    app.run(host='0.0.0.0',
            debug=True)

if __name__ == '__main__':
    main()
