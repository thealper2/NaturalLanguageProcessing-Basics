import nltk
from nltk.stem.porter import *

porter_stemmer = PorterStemmer()
word = 'sterilization'
print(porter_stemmer.stem(word))
