#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 10:32:01 2023

@author: santiago.egea@upf.edu

version 0.1
"""

# from pywsd.similarity import max_similarity, sim
try: # IF WORDNET2022 NOT FOUND, IT IS DOWNLOADED
    from nltk.corpus import wordnet as wn
except ImportError:
    print()
    print('(!) Wordnet 2022 not found...')
    print('(!) Standard WordNet will be used...')
    import nltk
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    from nltk.corpus import wordnet as wn
    
AVAILABLE_LANS = ['en', 'es', 'nl', 'ga']
POS_MAP = {'VERB': wn.VERB,'NOUN': wn.NOUN, 'PROPN': wn.NOUN, 'ADJ': wn.ADJ}
LAN_MAP = {'en' : 'eng', 'es' : 'spa', 'nl' : 'nld', 'ga' :'eng'}
class WSDisambiguater:
    def __call__(self, nlp_dict : dict, lan : str) -> list:
        """
        Applies Word Sense Disambiguation.
        Parameters
        ----------
        nlp_dict : dict
            A dict containing the information: LEMMAS, TOKEN AND UPOSTAG. This
            dict can be the output from the linguistic tagger. 

        lan : str
            String specifying the lanuage to handle. See AVAILABLE_LANS variable.

        Returns
        -------
        list : A list containing WordNet synsets.

        """
        assert lan in AVAILABLE_LANS, 'Unkown language. Available: {}'.format(AVAILABLE_LANS)
        sent_info = [(w,l,p) for w, l, p in zip(nlp_dict['TOKEN'], nlp_dict['LEMMA'],
                                                nlp_dict['UPOSTAG'])]
    
        lemma_sentence = ' '.join(nlp_dict['LEMMA'])
        tagged_sentence = []
        cached_synsets = {}
        for word, lemma, pos in sent_info:
            if pos in POS_MAP.keys(): # Checks if it is a content word
                ambiguous_synsets = wn.synsets(lemma, pos = POS_MAP[pos], lang = LAN_MAP[lan]) # First search in the WordNet
                ambiguous_synsets =  ambiguous_synsets if ambiguous_synsets else wn.synsets(lemma, lang = LAN_MAP[lan]) # Second search in the WordNet
                if ambiguous_synsets:
                    result = {}
                    for i in ambiguous_synsets: #wn.synsets(lemma, pos = POS_MAP[pos], lang = LAN_MAP[lan]):
                        result[i] = 0
                        for context_word in lemma_sentence.split():
                            _result = [0]
                            in_cache = context_word in cached_synsets.keys()
                            if not in_cache: cached_synsets[context_word] = wn.synsets(context_word, lang = LAN_MAP[lan])
                            context_synsets = cached_synsets[context_word]
                            for k in context_synsets:
                                _result.append(wn.path_similarity(i,k))
                            result[i] += max(_result)
                    result = sorted([(v,k) for k,v in result.items()],reverse=True)
                    synset = result[0][1].name()
                else: # In case the content word is not in WordNet.
                    synset = pos
            else:
                synset = pos
            tagged_sentence.append((word, synset))

        return list(map(lambda x : x[-1], tagged_sentence))






#%%%
# import sys
# import time
# sys.path.insert(1, '../LinguisticTagger')
# sys.path.insert(1, '../LinguisticTagger')
# from SignonNLUpipe import SignonNLUpipe

# sent1 = "Mi perro se llama Pimientos."
# sent1 = "Me gusta la pantalla de ese móvil."
# lan = 'es'
# nlp = SignonNLUpipe(lan)
# nlp_dict = nlp(sent1)

# sent1 = "I loved the screen on this phone."
# sent1 = "My dog is called Peppers."
# lan = 'en'
# nlp = SignonNLUpipe(lan)
# nlp_dict = nlp(sent1)

# sent1 = "Mijn hond heet Peppers."
# lan = 'nl'
# nlp = SignonNLUpipe(lan)
# nlp_dict = nlp(sent1)

# sent1 = "Peppers a thugtar ar mo mhadra."
# lan = 'ga'
# nlp = SignonNLUpipe(lan)
# nlp_dict = nlp(sent1)
# t0 = time.time()
# WSD = WSDisambiguater()
# print(time.time()-t0)
# print(WSD(nlp_dict, lan))











