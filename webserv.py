#!/usr/bin/python3

import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route("/coordinator", methods=['GET'])
def get_tasks():
    data = os.popen('tail -1  ./webserv.dat').read().rstrip('\n').split(',')
    coordinator = {'t': data[0], 'x': data[1], 'y': data[2]}
    return jsonify({'coordinator': coordinator})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)

