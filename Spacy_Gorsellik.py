import spacy
from spacy import displacy
from pathlib import Path

nlp = spacy.load('en_core_web_sm')
doc = nlp('Okan Buruk is the best coach.')
svg = displacy.render(doc, style='dep', jupyter=False)
path = Path('parsing.html')
path.open('w', encoding='utf-8').write(svg)