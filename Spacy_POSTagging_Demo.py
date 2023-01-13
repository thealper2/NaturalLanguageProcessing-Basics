import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("Okan Buruk is the best coach.")
for token in doc:
	print(token.text, token.pos_)
