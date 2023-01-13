import nltk
from nltk.tokenize import word_tokenize
from nltk import RegexpParser
from nltk import pos_tag

text = "Okan Buruk is the best coach."
words = word_tokenize(text)
tags = pos_tag(words)

# ? 0/1
# * 0/infinity
# + 1-INF

grammar = "NP: {<DT>?<JJ>*<NN>}"
parser = RegexpParser(grammar)
results = parser.parse(tags)
results.draw()