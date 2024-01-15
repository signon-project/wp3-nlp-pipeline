#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 17:22:32 2022

@author: upf
"""

import requests, json


with open('example-schema.json', 'r') as f:
    data = json.load(f)
    
data = {'App': {
  'sourceText': 'Hello Bob, How are you?',
  'sourceLanguage': 'ENG'}}

r = requests.post('http://127.0.0.1:5000', json =data)

print(r.json())

with open('output.json', 'w') as f:
    json.dump(r.json(), f)

