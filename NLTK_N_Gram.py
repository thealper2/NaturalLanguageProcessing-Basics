import nltk
from nltk.tokenize import word_tokenize
from nltk import bigrams, trigrams

# unigram = 1-gram
# bigram  = 2-gram
# trigram = 3-gram
# n-gram  = N-gram

text = """
Reverse Engineering, Pentesting, Web Security, Application Security
"""

words = word_tokenize(text)
print("UNIGRAM")
print(words)

print('BIGRAM')
for bigram in bigrams(words):
	print(bigram)

print('TRIGRAM')
for trigram in trigrams(words):
	print(trigram)
