import nltk
from nltk import ne_chunk

sentence = "Legendary scientist Albert Einstein is born in Ulm, Germany."
tokens = nltk.word_tokenize(sentence)
tagged_tokens = nltk.pos_tag(tokens)
entities = nltk.chunk.ne_chunk(tagged_tokens)
print(entities)
