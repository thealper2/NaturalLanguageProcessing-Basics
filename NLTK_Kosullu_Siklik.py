import nltk
from nltk.corpus import brown
from nltk.probability import ConditionalFreqDist

categories = brown.categories()
categories_words = [ (category, word)
					  for category in categories
					  	for word in brown.words(categories=category)]

distribution = ConditionalFreqDist(categories_words)
pronouns = ['I', 'you', 'he', 'she', 'it', 'we', 'they']
distribution.tabulate(conditions=categories, samples=pronouns)