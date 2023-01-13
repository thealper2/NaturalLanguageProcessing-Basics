import string

message = "Dil islemede kullanilan kutuphaneler: nltk, spacy, scikit-learn, zemberek."
print(message.translate(str.maketrans('', '', string.punctuation)))

