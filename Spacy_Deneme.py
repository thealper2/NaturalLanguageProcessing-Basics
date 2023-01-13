import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp('Python, Java, Lua, Ruby, Java, C/C++, JavaScript, PHP, C#.NET, HTML, CSS, JavaScript')

for token in doc:
	print(token.text)