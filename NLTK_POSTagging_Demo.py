import nltk

tokens = nltk.word_tokenize("Can you buy me a red gaming laptop ?")
print("Part of Speech: ", nltk.pos_tag(tokens))
