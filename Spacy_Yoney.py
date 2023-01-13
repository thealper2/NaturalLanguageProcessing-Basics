import spacy

nlp = spacy.load('en_core_web_md')

doc1 = nlp("software engineer")
doc2 = nlp("computer engineer")

print('Benzerlikler:')
for token1 in doc1:
	for token2 in doc2:
		print(token1, token2, token1.similarity(token2))