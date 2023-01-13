import nltk
from nltk.corpus import gutenberg

sentences = gutenberg.sents('shakespeare-macbeth.txt')
print('Cumleler: ', len(sentences))

words = gutenberg.words('shakespeare-macbeth.txt')
print('Sozcukler: ', len(words))