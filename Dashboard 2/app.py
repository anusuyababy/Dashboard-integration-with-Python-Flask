# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 14:05:24 2021

@author: DELL
"""
import os
from flask import Flask, render_template, abort, url_for, json, jsonify
import json
from flask import Flask, render_template, request



app = Flask(__name__)


with open('sample.json', 'r') as myfile:
    data = myfile.read()

@app.route('/')
def home():
    templateData = {
      'Teamcenter_FSC_Service' : 0,
      'T4S_GS' : 1,
      'Disk_usage_C' : 25,
      'Disk_usage_D' : 100
      }
    return render_template('index.html', **templateData)

if __name__ == '__main__':
    app.run(debug=True)