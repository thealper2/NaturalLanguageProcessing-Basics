import numpy as np
import gensim
from gensim.utils import simple_preprocess
from gensim import corpora
from gensim import models
from pprint import pprint

documents=["Hi, how old are you", "Who are you ?", "What are you doing ?"]
tokenizeds = [ simple_preprocess(document) for document in documents ]
dictionary = corpora.Dictionary()
corpus = [dictionary.doc2bow(tokenized, allow_update=True) for tokenized in tokenizeds]
tfidf = models.TfidfModel(corpus, smartirs='ntc')
print('TF*IDF:')
for document in tfidf[corpus]:
	print()
	for identity, frequency in document:
		print(dictionary[identity], ':', np.around(frequency, decimals=2))