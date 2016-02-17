#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from server import app

import os

@app.route('/')
def hello_world():
    greeting = os.environ.get('GREETING')
    return 'Hello, '+greeting

if __name__ == '__main__':
    print("Running server on http://localhost:5000")
    app.run(host='0.0.0.0', debug=True)
