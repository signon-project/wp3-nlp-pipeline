#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 18:12:25 2022

@author: euan.mcgill@upf.edu
Edited by santiago.egea@upf.edu (22/11/2023)

version 1
"""

import spacy as sp
import stanza
import spacy_stanza

AVAILABLE_LANS = ['en', 'es', 'nl', 'ga']


#%%############################################################################
'''                           SignonNLUpipe Class                           '''
###############################################################################

class SignonNLUpipe:
    
    def __init__(self, lan : str):
        """
        Initializes SignonNLUpipe.
        
        Parameters
        ----------
        lan : str
            String specifying the lanuage to handle. See AVAILABLE_LANS variable.

        """
        assert lan in AVAILABLE_LANS, 'Unkown language. Available: {}'.format(AVAILABLE_LANS)
        self.lan = lan
        if self.lan == 'en':
            self.nlp = sp.load('en_core_web_md')
            print("Loaded English (en_GB,IE) NL pipeline")
        elif self.lan == 'ga':
            stanza.download('ga')
            self.nlp = spacy_stanza.load_pipeline('ga')
            print("Loaded Irish (ga_IE) NL pipeline")
        elif self.lan == 'nl':
            self.nlp = sp.load('nl_core_news_md')
            print("Loaded Dutch (nl_BE,NL) NL pipeline")
        elif self.lan == 'es':
            self.nlp = sp.load('es_core_news_md')
            print("Loaded Spanish (es_ES) NL pipeline")

    def __call__(self, intext : str) -> dict:
        """
        Annotates intext with linguistic information.
        
        Parameters
        ----------
        intext : str
            The input text to process.

        Returns
        -------
        dict : A dictionary containing the linguistic tags.

        """
        # LINGUISTIC TAGGING
        doc = self.nlp(intext)
        l = len(doc)
        conll_dict = {
            # WORD ID, TOKEN AND LEMMA
            'ID' : ['' for _ in range(l)], 'TOKEN' : ['' for _ in range(l)],
            'LEMMA' : ['' for _ in range(l)],
            # PART-OF-SPEECH
            'UPOSTAG' : ['' for _ in range(l)],
            # MORPHOLOGY ANALYSIS
            'FEATS': ['' for _ in range(l)],
            # WORD DEPENDENCIES
            'HEAD' : ['' for _ in range(l)], 'DEPREL' : ['' for _ in range(l)],
            # NAME ENTITY RECOGNITION
            'NERTYPE' : ['' for _ in range(l)], 'NERPOS': ['' for _ in range(l)],
                  }
        
        # FILLING CONLL DICT
        for i,token in enumerate(doc): # now output to JSON with CoNLL-U column order
            conll_dict['ID'][i] = i+1
            conll_dict['TOKEN'][i] = str(token)
            conll_dict['LEMMA'][i] = token.lemma_
            conll_dict['UPOSTAG'][i] = token.pos_
            conll_dict['FEATS'][i] = str(token.morph)
            conll_dict['HEAD'][i] = token.head.i+1
            conll_dict['DEPREL'][i] = token.dep_
            conll_dict['NERTYPE'][i] = token.ent_type_
            conll_dict['NERPOS'][i] = token.ent_iob_
        return conll_dict
    
#%%############################################################################
'''                             Example of usage                            '''
###############################################################################    
    
'''

s_en = SignonNLUpipe('ENG')
print()
print(s_en('My dog is called Peppers'))
print()

s_es = SignonNLUpipe('SPA')
print()
print(s_es('Mi perro se llama Pimientos'))
print()
s_ga = SignonNLUpipe('GLE')
print()
print(s_ga('Peppers a thugtar ar mo mhadra'))
print()
s_nl = SignonNLUpipe('NLD')
print()
print(s_nl('Mijn hond heet Peppers'))
print()

'''

