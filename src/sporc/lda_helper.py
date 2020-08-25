import os
import sys
import glob
import gensim
import numpy as np
import multiprocessing as mp

FILE_DIR = os.path.dirname(os.path.abspath('__file__'))
sys.path.append(FILE_DIR)

def train_and_evaluate(triplets, p):
	'''Entry point.'''
	which_corpus = p['corpus']
	corpus_path = os.path.join(FILE_DIR, 'corpus/' + which_corpus + '/*.npy')
	corpus = np.array(glob.glob(corpus_path)) # filenames
	print('Files: ' + str(len(corpus)))
	return {'score': LDAModel(p['passes'], 
							  p['num_topics']).fit(which_corpus, corpus).evaluate(triplets),
			'parameters': p}

class LDAModel(object):
	def __init__(self, passes, num_topics):
		self.passes = passes
		self.num_topics = num_topics
		self.model = None
		self.dictionary = None
		self.bow = None
		self.corpus_ids = None
		self.corpus_iterator = None

	def get_dictionary(self, dictionary_path):
		'''Creates or loads dictionary.'''
		if not os.path.exists(dictionary_path):
			print('Creating dictionary...')
			dictionary = gensim.corpora.Dictionary(self.corpus_iterator)
			dictionary.save(dictionary_path)
		else:
			print('Loading dictionary...')
			dictionary = gensim.corpora.Dictionary.load(dictionary_path)
		return dictionary

	def get_bow(self, bow_path):
		'''Creates or loads bag-of-words vectors.'''
		if not os.path.exists(bow_path):
			print('Creating bag of word vectors...')
			bow = [self.dictionary.doc2bow(tokens) for tokens in self.corpus_iterator]
			gensim.corpora.MmCorpus.serialize(bow_path, bow)
		else:
			print('Loading bag of word vectors...')
			bow = gensim.corpora.MmCorpus(bow_path)
		return bow

	def fit(self, which_corpus, corpus):
		'''Gets the two main inputs to the LDA model (dictionary and bag-of-words vectors)
		and then trains LDA model.'''
		basepath = os.path.join(FILE_DIR, 'lda/' + which_corpus.replace('/', '_'))
		self.corpus_iterator = self.DocumentIterator(corpus)
		self.corpus_ids = [os.path.splitext(os.path.basename(x))[0] for x in corpus]
		self.dictionary = self.get_dictionary(basepath + '.dict')
		self.bow = self.get_bow(basepath + '.mm')
		cpus = mp.cpu_count()
		print('Training using ' + str(cpus) + ' cores...')
		self.model = gensim.models.LdaMulticore(corpus=self.bow,
												workers=cpus,
												num_topics=self.num_topics,
												id2word=self.dictionary,
												passes=self.passes)
		return self

	def evaluate(self, triplets):
		'''Calculates averaged accuracy of all given triplets,
		that ab is more similar than ac.'''
		print('Evaluating...')
		accuracy = 0
		for triplet in triplets:
			# Get filenames of papers A, B, C
			a_idx = self.corpus_ids.index(triplet[0])
			b_idx = self.corpus_ids.index(triplet[1])
			c_idx = self.corpus_ids.index(triplet[2])

			# Get vectors of papers A, B, C
			a = self.model[self.bow][a_idx]
			b = self.model[self.bow][b_idx]
			c = self.model[self.bow][c_idx]

			# Calculate accuracy
			ab_dist = gensim.matutils.hellinger(a, b)
			ac_dist = gensim.matutils.hellinger(a, c)
			if ab_dist > ac_dist:
				accuracy += 1
		return accuracy/len(triplets)

	class DocumentIterator(object):
		'''Iterator object that yields corpus file by file,
		so that we do not load the entire corpus into memory.'''
		def load_documents(self):
			for filename in self.filenames:
				try: 
					yield np.load(filename)
				except Exception as e:
					print('Error! ' + str(e))

		def __init__(self, filenames):
			self.filenames = filenames

		def __iter__(self):
			self.documents = self.load_documents() # Reset the iterator
			return self

		def __next__(self):
			tokens = next(self.documents)
			return tokens



