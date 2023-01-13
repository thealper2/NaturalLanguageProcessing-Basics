import spacy
from spacy import displacy
from collections import Counter
nlp = spacy.load('en_core_web_sm')
sentence = nlp('Okan Buruk is the best coach.')
print([(X.text, X.label_) for X in sentence.ents])
