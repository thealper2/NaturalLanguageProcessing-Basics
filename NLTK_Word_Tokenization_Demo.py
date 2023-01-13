import nltk
from nltk import word_tokenize
sentences = [ "Cumle 1", "Cumle 2", "Cumle 3"]

for sentence in sentences:
	print(word_tokenize(sentence))
