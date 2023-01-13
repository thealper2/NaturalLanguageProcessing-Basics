import gensim
from pprint import pprint
from gensim import corpora

documents = ["Veri bilimi ve yapay zeka alanında python kullanılır.", "Python, kolay bir dildir."]
words = [ [token for token in document.split() ] for document in documents ]
dictionary = corpora.Dictionary(words)
print('Dizgecikten Ozdeslige:')
print(dictionary.token2id)