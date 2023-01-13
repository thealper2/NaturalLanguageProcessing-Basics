import nltk
from nltk import sent_tokenize
text = """
Birinci cumle.
Ikinci cumle.
Ucuncu cumle.
"""
sentences = sent_tokenize(text)
for sentence in sentences:
	print(sentence)
