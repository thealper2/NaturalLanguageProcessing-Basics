import nltk
from nltk.corpus import gutenberg
from nltk import pos_tag
from nltk.probability import FreqDist

words = gutenberg.words('melville-moby_dick.txt')
taggeds = pos_tag(words)

tags = [tagged[1].lower() for tagged in taggeds]
print('Adliklar')
print(tags)

distribution = FreqDist(tags)
distribution.plot(title='Adlik Sirtliklari')

bins = distribution.B()
print('Kovalar')
print(bins)

numbers = distribution.N()
print('Sayilar')
print(numbers)

noun_count = distribution['nn']
print('Ad sayisi: ', noun_count)

noun_frequency = distribution.freq('nn')
print('Ad sikligi: ', noun_frequency)