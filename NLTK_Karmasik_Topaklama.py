import nltk
from nltk.tokenize import word_tokenize
from nltk import RegexpParser
from nltk import pos_tag

text = "Galatasaray won the UEFA cup."
words = word_tokenize(text)
tags = pos_tag(words)

# ? 0/1
# * 0/infinity
# + 1-INF

grammar = """NP: 
{<DT|PRP\$>?<JJS>*<NN>}
{<DT>?<JJ>*<NNP>+}
"""
parser = RegexpParser(grammar)
results = parser.parse(tags)
print(results)

results.draw()