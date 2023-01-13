import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
from collections import defaultdict
from nltk.stem import WordNetLemmatizer

text = 'Okan Buruk is the best coach.'
words = word_tokenize(text)

taggeds = pos_tag(words)

tag_dictionary = defaultdict(lambda: wn.NOUN)
tag_dictionary['J'] = wn.ADJ
tag_dictionary['V'] = wn.VERB
tag_dictionary['R'] = wn.ADV

lemmatizer = WordNetLemmatizer()
for word, tag in taggeds:
	wn_tag = tag_dictionary[tag[0]]
	lemma = lemmatizer.lemmatize(word, wn_tag)
	print(word, ':', tag, ' > ', wn_tag, ' # ', lemma)