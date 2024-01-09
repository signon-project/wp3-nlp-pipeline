# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 11:34:58 2023

@author: SNT
"""
import sys
sys.path.insert(1, '../LinguisticTagger')
sys.path.insert(1, '../TextNormalizer')
from WSDisambiguater import WSDisambiguater
from TextNormalizer import TextNormalizer
from SignonNLUpipe import SignonNLUpipe

#%%############################################################################
'''                                ENGLISH                                  '''
###############################################################################
""""""
all_senses_path_similarity = []

ori_english = [ "Enjoyable",
                "Cockroaches everywhere!",
                "Awesome! I will come back!",
                "Excellent room and well mannered service!",
                "The evening help was rude and none attentive.",
                "The hotel was perfect for our girlfriend get-away.",
                "In town to Christmas shop and spend time with family.",
                "Very comfortable rooms, will stay again when in the area.",
                "Very restful and quite. Also had a nice pool to relax in.",
                "The hotel was beautiful and the staff was awesome. One of the best beaches in mexico"]

dirty_sentences = [
    'Enjoiable.',
    'Cockroaches everywhere !!!!!!~@!',
    'Awesume !!!!!! I will come back !',
    'Excellent room and welll mannered service!',
    'The evening help was rude and none atentive.',
    'The hotel was perfect for our girtfriend get-away.',
    'In town to Christmass shop and spand time with family.',
    'Very comfortable roms, will stay again when in the area.',
    'Very restful and quite..... Also had a nice pool to relax in. $',
    'The hutel was beautiful and the stafff was awesome. One of the best beeches in mexico',
    ]
lan = 'en'


WSD = WSDisambiguater()
nlp = SignonNLUpipe(lan)
text_normalizer = TextNormalizer()
#%%
normalized = [text_normalizer(s, lan) for s in dirty_sentences]
linguistic_tags = [nlp(s) for s in normalized]
senses_path_similarity = [WSD(s, lan) for s in linguistic_tags]

for o, d, n, ws in zip(ori_english, dirty_sentences, normalized, senses_path_similarity):
    print('D:',d)
    print('N:',n)
    print('R:',o)
    print('S:','|'.join(ws))

all_senses_path_similarity += senses_path_similarity

#%%############################################################################
'''                                SPANISH                                  '''
###############################################################################
""""""


ori_spanish = [ "Adorable.",
                "¡Hay cucarachas por todas partes!",
                "¡Increíble! ¡Volveré!",
                "Excelente habitación y muy buen servicio.",
                "Los trabajadores de la tarde fueron maleducados y poco atentos.",
                "El hotel fue perfecto/ideal para nuestra escapada en pareja.",
                "En la ciudad para hacer compras navideñas y estar en familia.",
                "Las habitaciones son muy cómodas, volveré cuando esté otra vez por la zona.",
                "Lugar apacible y tranquilo. También dispone de una piscina para desconectar.",
                "El hotel era precioso y los trabajadores increíbles. Una de las mejores playas de México."]


dirty_sentences = [
    'Adorable. =@', 
    '¡Hay cucarachas por todes partes!',
    '¡Increíble! ¡Bolveré!',
    'Excelente habitación y muy buen servicio....',
    'Los trabajadores de la tarde fueron maleducados y poco attentos.',
    'El hutel fue ideal para nuestra escapada en pareja.',
    'En la ciudad para hacer compras navidenas y estar en famillia.',
    'Las habitaciones son muy comodas, volvere cuando este otra vez por la zona.',
    'Lugar apacible y trankilo.... Tambien dispone de una piscina para desconectar.',
    'El hotel era precioso y los trabajadores increíbles. Una de las mejores platjas de México.',
    ]
lan = 'es'

WSD = WSDisambiguater()
nlp = SignonNLUpipe(lan)
text_normalizer = TextNormalizer()

#%%
normalized = [text_normalizer(s, lan) for s in dirty_sentences]
linguistic_tags = [nlp(s) for s in normalized]
senses_path_similarity = [WSD(s, lan) for s in linguistic_tags]

for o, d, n, ws in zip(ori_spanish, dirty_sentences, normalized, senses_path_similarity):
    print('R:',o)
    print('I:',d)
    print('N:',n)
    print('S:','|'.join(ws))
all_senses_path_similarity += senses_path_similarity

#%%############################################################################
'''                                   IRISH                                 '''
###############################################################################    
"""

ori_irish = [
    "Taitneamhach",
    "Ciaróga dhubha i ngach áit!",
    "Iontach ! Tiocfaidh mé ar ais!",
    "Seomra iontach, agus seirbhís dea-bhéasach.",
    "Bhí an fhoireann tráthnóna drochbhéasach, agus níor thug siad aird dúinn.",
    "Bhí an t-óstán foirfe dár laethanta saoire chailíní.",
    "Tá mé ar an mbaile chun siopadóireacht a dhéanamh don Nollaig, agus am a chaitheamh leis an teaghlach.",
    "Seomraí an-chompordach. D'fhanfainn arís dá mbeinn sa cheantar.",
    "An-shuaimhneach agus ciúin. Bhí linn snámha deas ann freisin chun scíth a ligean ann.",
    "Bhí an t-óstán go hálainn, agus bhí an fhoireann ar fheabhas. Tá sé ar cheann de na tránna is fearr i Meicsiceo"
]


dirty_sentences = [
    'Taitneamhachh',
    'Ciarója dhubha i ngach áit !!!!!',
    'Iontach!!!!!! Tiucfaidh mé ar ais!',
    'Seomra ontach, agus seirbhís dea-héasach. $)&',
    'Bhí anm fhoireannn tráthnóna drochbhéasach, agus níor thog siad aird dúinn.',
    'Bí an tóstán fojrfe dár laethanta saoire chailíní.',
    'Ta me ar an mbaile chun siopadóireacht a dhéanamh don Nollaig, agus am a chaitheamh leis an teaghlach.',
    "Seomraí an-chompordach....... D'fhanfainn arís da mbeinn sa cheantar.",
    "An-shuaimhneach agus ciuin. Bhí linn snámha dees ann freisin chun scíth a ligean ann.",
    "Bhí an tóstán go hálainn, agus bhí an fhoireann ar fheabhas. Tá sé ar chheann de na tránna is fear i Meicsiceo"]
        

lan = 'ga'

nlp = SignonNLUpipe(lan)
text_normalizer = TextNormalizer()
normalized = [text_normalizer(s, lan) for s in dirty_sentences]
linguistic_tags = [nlp(s) for s in normalized]
#%%
for o, d, n in zip(ori_irish, dirty_sentences, normalized):
    print('R:',o)
    print('I:',d)
    print('N:',n)
"""
#%%############################################################################
'''                                   DUTCH                                 '''
###############################################################################    
""""""

ori_dutch = [
    "Heb genoten.",
    "Overal kakkerlakken!",
    "Geweldig! Ik kom zeker terug!",
    "Uitstekende kamer en goede service!",
    "De avondmedewerker was onbeschoft en niet attent.",
    "Het hotel was perfect voor ons vriendinnen uitje.",
    "We waren in de stad om kerstinkopen te doen en tijd door te brengen met familie.",
    "Zeer comfortabele kamers, ik zal er zeker opnieuw verblijven wanneer ik weer in de buurt ben.",
    "Heel rustgevend en rustig. Er was ook een mooi zwembad om in te ontspannen.",
    "Het hotel was prachtig en het personeel was geweldig. Een van de beste stranden in Mexico.",
    ]

dirty_sentences = [
    "Heb genotenn.",
    "Overal kakkerlakken!!!!!!!&/(",
    "Geweldig!!!!!! Ik kom zekerr terug!",
    "Uitstekende kamer en goede service!",
    "De avondmedewerkar wes onbeschoft en niet atttent.",
    "Het hotel was perfect voor ons vriendinnen uitje.",
    "We waren in de stud om kerstinkopen te doen en tijd door te brengen met familia",
    "Zear comfortabele kamers, ik zal er zeker opnieuw verbliiven wanneer ik weer in de buurt ben.",
    "Heel rustgevend en rustig...... Er was ookj een mooi zwembad om in te ontspannen.",
    "Het hotel was prchtig en het personeil was geweldig. Een van de beste stranden in Mexico."]
        
lan = 'nl'


nlp = SignonNLUpipe(lan)
text_normalizer = TextNormalizer()
WSD = WSDisambiguater()

normalized = [text_normalizer(s, lan) for s in dirty_sentences]
linguistic_tags = [nlp(s) for s in normalized]
senses_path_similarity = [WSD(s, lan) for s in linguistic_tags]

for o, d, n, ws in zip(ori_dutch, dirty_sentences, normalized, senses_path_similarity):
    print('R:',o)
    print('I:',d)
    print('N:',n)
    print('S:','|'.join(ws))
all_senses_path_similarity += senses_path_similarity
#%%############################################################################
'''                              DEFINITIONS                                '''
###############################################################################
""""""      
from nltk.corpus import wordnet2022 as wn

all_senses = set([s for senses in all_senses_path_similarity for s in senses])
definitions = {}

for s in all_senses:
    # if s not in ['DET', 'PUNCT', 'ADJ', 'ADP', '']:
    try:
        definitions[s] = wn.synset(s).definition()
    except ValueError:
        pass
definitions = dict(sorted(definitions.items()))
#%%
for name, d in definitions.items():
    print(name+':', d)
