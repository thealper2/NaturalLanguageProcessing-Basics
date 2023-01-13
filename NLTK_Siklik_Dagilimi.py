import nltk
import matplotlib.pyplot
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

text = """
A B C D E F G A A H C K K G L M N I S U A L A D C E F G N B O
"""

words = word_tokenize(text)
distribution = FreqDist(words)
distribution.plot(title='Frequency')

print('KOVALAR')
print(distribution.B())

print('SAYILAR')
print(distribution.N())

count = distribution['A']
print('Frequency: ', count)

freq = distribution.freq('A')
print('Frequency: ', freq)