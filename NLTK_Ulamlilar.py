import nltk
from nltk.corpus import brown

sentences = brown.sents()
print('Cumleler: ' , len(sentences))

words = brown.words()
print('Sozcukler: ' , len(words))

categories = ['fiction', 'science_fiction']

sentences = brown.sents(categories=categories)
print('Tumceler' , len(sentences))

words = brown.words(categories=categories)
print('Sozcuk sayisi:' , len(words))