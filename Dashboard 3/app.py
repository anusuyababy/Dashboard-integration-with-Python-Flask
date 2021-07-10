# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 15:50:17 2021

@author: DELL
"""

import os
from flask import Flask, render_template, abort, url_for, json, jsonify
import json
from flask import Flask, render_template, request



app = Flask(__name__)




@app.route('/')
def home():
    with open('sample.json', 'r') as myfile:
        data = myfile.read()
    
    return render_template('index.html', jsonfile=json.dumps(data))

if __name__ == '__main__':
    app.run(debug=True)