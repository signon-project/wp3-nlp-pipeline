# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 09:43:09 2023

@author: SNT
"""

#%%############################################################################
'''                               IMPORTS                                   '''
###############################################################################

from flask import Flask, request, json, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

import colored
import sys
from LinguisticTagger.SignonNLUpipe import SignonNLUpipe
from WSD.WSDisambiguater import WSDisambiguater
from TextNormalizer.TextNormalizer import TextNormalizer

#%%############################################################################
'''               GLOBAL VARIABLES & SERVER INITIALIZATION                  '''
###############################################################################

SERVER_PORT = 5000
TEXT_NORMALIZER = None
LINGUISTIC_TAGGERS = {}
WSD = None
AVAILABLE_LANS = ['ENG', 'GLE', 'DUT', 'SPA']
LAN_MAP = {'ENG' : 'en', 'SPA' : 'es', 'DUT' : 'nl', 'GLE' :'ga'}

#%%############################################################################
'''                             API FUNCTIONS                               '''
###############################################################################
@app.route('/', methods=['POST'])
def process():
    global TEXT_NORMALIZER, LINGUISTIC_TAGGERS, WSD
    input_dict = request.get_json(force = True)
    
    lan = input_dict['App']['sourceLanguage']
    assert lan in AVAILABLE_LANS, 'Unkown language. Available: {}'.format(AVAILABLE_LANS)
    text = input_dict['App']['sourceText']
    
    normalized = TEXT_NORMALIZER(text, lan = LAN_MAP[lan])   # TEXT NORMALIZATION
    linguistic_tags = LINGUISTIC_TAGGERS[lan](text)          # LIN TAGGING
    wsd_output = WSD(linguistic_tags, lan = LAN_MAP[lan])    # WSD
    output_json = {'normalised' : normalized, 'lin_tags' : linguistic_tags,
                   'wsd' : wsd_output}

    return jsonify(output_json)

#%%############################################################################
'''                          SYSTEM FUNCTIONS                               '''
###############################################################################
def loadSystem():
    global TEXT_NORMALIZER, LINGUISTIC_TAGGERS, WSD

    # TEXT NORMALIZER
    print('[*] Loading text normalizer...' , end='')
    TEXT_NORMALIZER = TextNormalizer()
    print(colored.attr(1)+colored.fg(2)+'Ok'+colored.attr(0))

    # LINGUISTIC TAGGERS
    print('[**] Loading linguistic taggers...' , end='')
    for l in AVAILABLE_LANS:
        LINGUISTIC_TAGGERS[l] = SignonNLUpipe(lan = LAN_MAP[l])
    print(colored.attr(1)+colored.fg(2)+'Ok'+colored.attr(0))
    
    # WSD MODULE
    print('[***] Loading Word-Sense Disambiguation module...' , end='')
    WSD = WSDisambiguater()
    print(colored.attr(1)+colored.fg(2)+'Ok'+colored.attr(0))

#%%############################################################################
'''                                 MAIN                                    '''
###############################################################################    

def main():
    loadSystem()
    app.run(host = '0.0.0.0', port = SERVER_PORT)

if __name__ == '__main__':
    main()

#%%############################################################################
'''                          DEBUG PURPOSES                                 '''
###############################################################################
# import time
# tLoad = time.time()
# loadSystem()

# with open('example-schema.json', 'r') as f:
#     example_dict = json.load(f)

# print(process(example_dict))
