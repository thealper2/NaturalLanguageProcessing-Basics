import string

stop_words = ['acaba', 've', 'bir', 'bircok', 'ama', 'icin']
message = "Metin icindeki a ve b kelimelerini temizlemek icin bircok yontem kullanilabilir."

s1 = set(stop_words)
s2 = set(message.lower().split())

print("Stopwords: ")
print(s1.intersection(s2))
