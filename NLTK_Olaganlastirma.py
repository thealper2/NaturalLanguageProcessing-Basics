import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

words = ['drink', 'drank', 'drinking', 'drinks']

stems = []
stemmer = PorterStemmer()
for word in words:
	stem = stemmer.stem(word)
	stems.append(stem)

print('STEM')
print(stems)

lemmas = []
lemmatizer = WordNetLemmatizer()
for word in words:
	lemma = lemmatizer.lemmatize(word)
	lemmas.append(lemma)

print('LEMMA')
print(lemmas)
