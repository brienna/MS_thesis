import os
import glob
import sys
import numpy as np
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from scipy.spatial.distance import cosine as cosine_distance

FILE_DIR = os.path.dirname(os.path.abspath('__file__'))
sys.path.append(FILE_DIR)

def train_and_evaluate(triplets, p, model_id):
    vector_size = p['vector_size']
    dm = p['dm']
    which_corpus = p['corpus']
    datapath = os.path.join(FILE_DIR, 'abstracts/' + which_corpus + '/*.npy')
    data = np.array(glob.glob(datapath))[:1000]
    return {model_id: {'parameters': p, 'score': Doc2VecModel(model_id, which_corpus, dm, vector_size).fit(data).evaluate(triplets)}}

class Doc2VecModel(object): 
    def __init__(self, model_id, which_corpus, dm=1, vector_size=100, window=1):
        '''Must match all parameters in my param dict.'''
        self.model = None
        self.model_id = model_id
        self.vector_size = vector_size
        self.window = window
        self.dm = dm
        self.which_corpus = which_corpus

    def fit(self, data):
        self.model = Doc2Vec(vector_size=self.vector_size, 
                             window=self.window, 
                             dm=self.dm, 
                             epochs=10,
                             alpha=0.025, 
                             min_alpha=0.001)
        tagged_docs = self.DocumentIterator(data)
        self.model.build_vocab(tagged_docs)
        self.model.train(tagged_docs, total_examples=self.model.corpus_count, epochs=self.model.epochs)
        return self

    def get_vector(self, doc_id):
        '''Takes a Pandas row for a paper.'''
        loaded = np.load(os.path.join(FILE_DIR, 'abstracts/' + self.which_corpus + '/' + doc_id + '.npy'))
        return self.model.infer_vector(loaded)

    def evaluate(self, triplets):
        '''Calculates averaged accuracy of all given triplets.
        [accuracy that ab is more similar than ac, ab more similar than bc]'''
        accuracies = [0, 0]
        for triplet in triplets:
            a_vector = self.get_vector(triplet[0])
            b_vector = self.get_vector(triplet[1])
            c_vector = self.get_vector(triplet[2])
            ab_dist = cosine_distance(a_vector, b_vector)
            ac_dist = cosine_distance(a_vector, c_vector)
            bc_dist = cosine_distance(b_vector, c_vector)
            if ab_dist > ac_dist and ab_dist > bc_dist:
                accuracies[0] += 1
                accuracies[1] += 1
            elif ab_dist > ac_dist and ab_dist < bc_dist:
                accuracies[0] += 1
            elif ab_dist < ac_dist and ab_dist > bc_dist:
                accuracies[1] += 1
        return max([accuracies[0]/len(triplets), accuracies[1]/len(triplets)])

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