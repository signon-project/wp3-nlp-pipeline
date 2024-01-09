# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 16:31:42 2023

@author: santiago.egea@upf.edu

version 1
"""
import os, json
from spylls.hunspell import Dictionary
from difflib import SequenceMatcher
from wordfreq import word_frequency
import re, string#, contractions

joinPaths = lambda p : os.path.join(*p)
AVAILABLE_LANS = ['en', 'es', 'nl', 'ga']
ALLOWED_PUNCT = r'.,!?¿¡'
NOT_ALLOWED_PUNCT = r'"#$%&\'()*+-/:;<=>@[\\]^_`{|}~'

#%%############################################################################
'''                           TextNormalizer Class                          '''
###############################################################################
class TextNormalizer:
    def __init__(self):
        """
        Initializes TextNormalizer
        """
        module_path = os.path.dirname(os.path.realpath(__file__))
        # Loads Hunspell dictionaries
        self.dicts = dict(zip(AVAILABLE_LANS,
                              [Dictionary.from_files(joinPaths([module_path, '.','dicts',lan, lan]))
                               for lan in AVAILABLE_LANS]))

    def similar(self, a : str, b : str) -> float:
        """
        Measures the similarity between words at character level. 
        
        Parameters
        ----------
        intext : str
            The input text to process.

        Returns
        -------
        dict : A dictionary containing the linguistic tags.

        """
        return SequenceMatcher(None, a, b).ratio()

    def check_word(self, word : str, lan : str) -> str:
        """
        Applies mispelling checking to a word and a language.
        
        Parameters
        ----------
        word : str
            The word to correct.
            
        lan : str
            String specifying the lanuage to handle. See AVAILABLE_LANS variable.

        Returns
        -------
        str : The corrected word.

        """
        assert lan in AVAILABLE_LANS, 'Unkown language. Available: {}'.format(AVAILABLE_LANS)
        dictionary = self.dicts[lan]
        if dictionary.lookup(word): return word
        suggestions = list(dictionary.suggest(word))
        if word in suggestions:
            correct = word
        else:
            word_score = [(s, self.similar(s,word),word_frequency(s, lan)) for s in suggestions]
            word_score.sort(key=lambda x : x[1]*x[2])
            try:
                correct = word_score[-1][0]
            except IndexError:
                pass
        return correct


    def regex_ops(self, sentence : str) -> str:
        """
        Regex operations to normalize punctuations.
        
        Parameters
        ----------
        sentence : str
            The sentence to normalize.

        Returns
        -------
        str : Normalized sentence.

        """
        sentence = ''.join([c if c not in NOT_ALLOWED_PUNCT else '' for c in sentence]) # REMOVES NOT ALLOWED PUNCTUATION
        sentence = re.sub(r'(\W)(?=\1)', '', sentence)                          # REMOVES EXTRA PUNCTUATIONS: 'Ahh!!!' => 'Ahh!'
        sentence = re.sub(r'(['+ALLOWED_PUNCT+'])', r' \1 ', sentence)           # ADDES WHITESPACE BEFORE/AFTER PUNCTUATIONS: 'Ahh!!!' => 'Ahh!'
        sentence = re.sub(r' +', r' ', sentence)                                  # REMOVES MULTIPLE WITHSPACES
        sentence = sentence if sentence[-1] != ' ' else sentence[:-1]           # REMOVES WHISPACE AT THE END OF A SENTENCE
        sentence = sentence if sentence[0] != ' ' else sentence[1:]             # REMOVES WHISPACE AT THE BEGINING OF A SENTENCE
        return sentence

    def __call__(self, sentence : str, lan : str) -> str:
        """
        Call function to apply the text normalizer.
        
        Parameters
        ----------
        sentence : str
            The sentence to normalize.

        lan : str
            String specifying the lanuage to handle. See AVAILABLE_LANS variable.

        Returns
        -------
        str : Normalized sentence.

        """
        assert lan in AVAILABLE_LANS, 'Unkown language. Available: {}'.format(AVAILABLE_LANS)
        sentence = self.regex_ops(sentence)  # REMOVE STRANGE PUNCTUATIONS
        correct_sen = [self.check_word(word, lan) if word not in ALLOWED_PUNCT else word
                       for word in sentence.split(' ')]
        return ' '.join(correct_sen)



#%%############################################################################
'''                             Example of usage                            '''
###############################################################################  
'''

# ENGLISH
lan = 'en'
sentence = "My dogg is called Peppers!!! &&"
text_normalizer = TextNormalizer()
print(text_normalizer(sentence, lan))
EXAMPLES
# SPANISH
lan = 'es'
sentence = '¿Un perrro llamao Pimientos? /@'
print(text_normalizer(sentence, lan))
# IRISH
lan = 'ga'
sentence = 'Madra ar a dtugtar Peppers.'
print(text_normalizer(sentence, lan))
# DUTCH
lan = 'nl'
sentence = 'Honnd genaamd Peppers.'
print(text_normalizer(sentence, lan))

'''




