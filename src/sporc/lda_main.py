
from sklearn.model_selection import ParameterGrid
import numpy as np
from lda_helper import train_and_evaluate
import json

def main():
	# Initializations
	scores_path = 'lda_scores.txt'
	triplets = np.load('20000_triplets.npy')
	params = {'corpus': ['abstracts/and_stopword_removal',
                         'abstracts/and_stemming',
                         'abstracts/and_lemmatization',
                         'abstracts/basic_preprocessing',
                         'fulltexts/basic_preprocessing',
                         'fulltexts/and_stemming',
                         'fulltexts/and_lemmatization',
                         'fulltexts/and_stopword_removal'],
			  'passes': [4],
			  'num_topics': [6]}
	tasks = list(ParameterGrid(params))

	# Train and evaluate model
	score = train_and_evaluate(triplets, tasks[0])
	with open(scores_path, 'w+') as f:
		json.dump(score, f)

if __name__ == '__main__':
	main()
