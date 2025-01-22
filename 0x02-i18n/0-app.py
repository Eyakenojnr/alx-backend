#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """
    Handles '/' route
    """
    return render_template('0-index.html')
