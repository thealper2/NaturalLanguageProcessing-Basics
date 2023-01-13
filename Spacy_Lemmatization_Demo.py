import spacy
nlp = spacy.load('en_core_web_sm')
word = nlp('serialization')
for token in word:
	print(token.lemma_)
	
