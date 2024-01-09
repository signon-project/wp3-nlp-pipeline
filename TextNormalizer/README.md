# SignON TextNormalizer

This repo implements the class TextNormalizer for SignON.
Hunspell: https://github.com/hunspell/hunspell

## Example of usage
```python

# ENGLISH
lan = 'en'
sentence = 'Dogg caled Peppers!!! &&'
text_normalizer = TextNormalizer()
print(text_normalizer(sentence, lan)

# SPANISH
lan = 'es'
sentence = '¿Un perro llamao Pimientos? /@'
print(text_normalizer(sentence, lan))

# IRISH
lan = 'ga'
sentence = 'Madra ar a dtugtar Peppers.'
print(text_normalizer(sentence, lan))

# DUTCH
lan = 'nl'
sentence = 'Honnd genaamd Peppers.'
print(text_normalizer(sentence, lan))
```
#### Output:
    English: Dog called Peppers !
    Spanish: ¿ Un perro llamado Pimientos ?
    Irish: Madra a a dtugtar Peters
    Dutch: Hond genaamd Pepers
