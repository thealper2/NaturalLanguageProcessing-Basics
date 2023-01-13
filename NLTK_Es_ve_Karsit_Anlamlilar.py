import nltk
from nltk.corpus import wordnet

word = 'power'

# Es Anlamlilari
synonym_list = []
antonym_list = []
for synset in wordnet.synsets(word):
	for lemma in synset.lemmas():
		synonym_list.append(lemma.name())
		if lemma.antonyms():
			antonym_list.append(lemma.antonyms()[0].name())

synonym_set = set(synonym_list)
print('ES ANLAMLILAR')
print(synonym_set)
print()
print('KARSIT ANLAMLILAR')
antonym_set = set(antonym_list)
print(antonym_set)