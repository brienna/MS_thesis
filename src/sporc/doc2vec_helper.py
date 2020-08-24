import os
import glob
import sys
import numpy as np
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from scipy.spatial.distance import cosine as cosine_distance


FILE_DIR = os.path.dirname(os.path.abspath('__file__'))
#CORPUS_DIR = '/Volumes/ARCHIVES/Thesis/data/' # uncomment if using on my local machine
sys.path.append(FILE_DIR)

def train_and_evaluate(triplets, p):
    which_corpus = p['corpus']
    corpuspath = os.path.join(FILE_DIR, 'corpus/' + which_corpus + '/*.npy') 
    #corpuspath = os.path.join(CORPUS_DIR, 'corpus/' + which_corpus + '/*.npy') # uncomment if using on my local machine
    corpus = np.array(glob.glob(corpuspath))
    return {'score': Doc2VecModel(p['dm'],
                                  p['vector_size'], 
                                  p['epochs'],
                                  p['window'],
                                  p['hs'],
                                  p['min_count']).fit(corpus).evaluate(triplets),
            'parameters': p}

class Doc2VecModel(object): 
    def __init__(self, 
                 dm,
                 vector_size,
                 epochs,
                 window,
                 hs,
                 min_count):
        '''Must match all parameters in my param dict.'''
        self.model = None
        self.dm = dm
        self.vector_size = vector_size
        self.epochs = epochs
        self.window = window
        self.hs = hs
        self.min_count = min_count

    def fit(self, corpus):
        tagged_docs = self.DocumentIterator(corpus)
        self.model = Doc2Vec(dm=self.dm, 
                             vector_size=self.vector_size, 
                             epochs=self.epochs,
                             window=self.window, 
                             hs=self.hs,
                             min_count=self.min_count,
                             alpha=0.025,
                             min_alpha=0.001)
        tagged_docs = self.DocumentIterator(corpus)
        self.model.build_vocab(tagged_docs)
        self.model.train(tagged_docs, total_examples=self.model.corpus_count, epochs=self.model.epochs)
        return self

    def evaluate(self, triplets):
        '''Calculates averaged accuracy of all given triplets,
        that ab is more similar than ac.'''
        accuracy = 0
        for triplet in triplets:
            a_vector = self.model.docvecs[triplet[0]]
            b_vector = self.model.docvecs[triplet[1]]
            c_vector = self.model.docvecs[triplet[2]]
            ab_dist = cosine_distance(a_vector, b_vector)
            ac_dist = cosine_distance(a_vector, c_vector)
            bc_dist = cosine_distance(b_vector, c_vector)
            if ab_dist > ac_dist:
                accuracy += 1
        return accuracy/len(triplets)

    class DocumentIterator(object):
        def load_documents(self):
            for filename in self.filenames: 
                loaded_file = np.load(filename)
                tag = os.path.splitext(os.path.basename(filename))[0]
                abstract = TaggedDocument(words=loaded_file, tags=[tag])
                try:
                    yield abstract
                except Exception as e:
                    print('Error!' + str(e))
                finally:
                    del loaded_file
                    # print('Closed ' + tag)
                    
        def __init__(self, filenames):
            self.filenames = filenames
            #self.documents = self.load_documents()

        def __iter__(self):
            self.documents = self.load_documents() # Reset the iterator
            return self
        
        def __next__(self):
            abstract = next(self.documents)
            return abstract