#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 17:22:32 2022

@author: upf
"""

import requests, json


with open('example-schema.json', 'r') as f:
    data = json.load(f)



r = requests.post('http://127.0.0.1:5000', json =data)

print(r.json())

with open('output.json', 'w') as f:
    json.dump(r.json(), f)


'''
curl -X 'POST'   'http://localhost:8080/message'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{
    "App": {
      "sourceKey": "NONE",
      "sourceText": "Hola como estas?",
      "sourceLanguage": "SPA",
      "sourceMode": "TEXT",
      "sourceFileFormat": "NONE",
      "sourceVideoCodec": "NONE",
      "sourceVideoResolution": "NONE",
      "sourceVideoFrameRate": -1,
      "sourceVideoPixelFormat": "NONE",
      "sourceAudioCodec": "NONE",
      "sourceAudioChannels": "NONE",
      "sourceAudioSampleRate": -1,
      "translationLanguage": "ENG",
      "translationMode": "TEXT",
      "appInstanceID": "0000",
      "appVersion": "0.1.0",
      "T0App": 1508484583259
    }
  }'
     AÑADIR A LO QUE LLEGA AL DISPATCHER
    "NLU": {
      "sourceText": "Hola como estas?",
      "sourceLanguage": "SPA",
      "translationLanguage": "ENG",
      "T3App": 1508484583259
        }
    
    '''