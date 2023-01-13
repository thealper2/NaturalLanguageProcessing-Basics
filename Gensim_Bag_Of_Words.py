import gensim
from gensim import corpora
from gensim.utils import simple_preprocess
from pprint import pprint

documents = ["Tell me who i am ?", "I am doing nothing."]
tokens = [ simple_preprocess(document) for document in documents ]

dictionary = corpora.Dictionary(tokens)
corpus = [ dictionary.doc2bow(token, allow_update=True) for token in tokens ]
print('Sozcuk Torbasi:')
pprint(corpus)