import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorized, TfidfTransformer

vectorizer = TfidfVectorizer()

text1 = """Python, Java, Lua, Ruby, Java, C/C++, JavaScript, PHP, C#.NET, HTML, CSS, JavaScript"""
text2 = """Python, Java, Lua, Ruby, Java, C/C++, JavaScript, PHP, C#.NET, HTML, CSS, JavaScript"""

corpus = [text1, text2]
vectorizer.fit(corpus)
terms = vectorizer.transform(corpus)
print('Ozellik Adlari:')
print(vectorizer.get_feature_names())
print('Belge Adalgilari:')
print(terms)
print('Belge Betileri:')
print(terms.shape)
print('Sozcuk Sayilari:')
print(terms.toarray())