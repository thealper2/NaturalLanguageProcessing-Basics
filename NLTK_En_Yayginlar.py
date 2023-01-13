import nltk
import Featuresets as feature
from nltk.corpus import movie_reviews

words = feature.find_cleans_for_unigrams(movie_reviews.words())
commons = feature.find_common_words(words)
print(commons[:10])

featuresets = feature.load_featuresets_for_commons(movie_reviews, commons)
print(featuresets[0])