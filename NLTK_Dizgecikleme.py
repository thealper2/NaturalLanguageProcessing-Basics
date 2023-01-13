import nltk
from nltk.tokenize import RegexpTokenizer

text = """
Bu cumle, her bir isaret; sozcuklere ayrilacak.
"""

regex = RegexpTokenizer("[\w']+")
justs = regex.tokenize(text)
print('Yalnizca Sozcukler')
print(justs)