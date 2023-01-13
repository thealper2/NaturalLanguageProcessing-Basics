import Featuresets as feature
from nltk.corpus import movie_reviews
from nltk import NaiveBayesClassifier
from nltk import classify
from nltk.tokenize import word_tokenize

def test_classifier_for_unigrams(classifier, text):
	words = word_tokenize(text)
	featureset = feature.create_featureset_for_unigram(words)
	probability = classifier.prob_classify(featureset)
	print('Olasilik:', probability.max())
	print('Olumlu:', probability.prob('pos'))
	print('Olumsuz:', probability.prob('neg'))

featuresets_pos = feature.load_featuresets_for_unigrams_by_category(movie_reviews, 'pos')
featuresets_neg = feature.load_featuresets_for_unigrams_by_category(movie_reviews, 'neg')

train_set = featuresets_pos[200:] + featuresets_neg[200:]
test_set = featuresets_pos[:200] + featuresets_neg[:200]

classifier = NaiveBayesClassifier.train(train_set)
accuracy = classify.accuracy(classifier, test_set)
print('Dogruluk:', accuracy)
importants = [feature for (feature, value) in classifier.most_informative_features(10)]
print('Onemliler:')
print(importants)

print('Olumsuz')
text_disliked = "I hated it. The movie was bad. It was terrible!"
test_classifier_for_unigrams(classifier, text_disliked)

print('Olumlu')
text_liked = "I liked it. The movie was good. It was excellent!"
test_classifier_for_unigrams(classifier, text_liked)