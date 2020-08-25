'''
Sets absolute and relative filepaths.
These filepaths are used by all code in this project.

To generate pickled filepaths.p, run `python set_filepaths.py` 

If running code on a different machine, e.g. the cloud, 
consider pickling the new filepaths or using relative filepaths.
'''

import pickle

root = '/Volumes/ARCHIVES/Thesis/'
pickle_path = root + 'data/globals.p'

absolute_filepaths = {'metadata': root + 'data/metadata.csv',
  					  'conversion_log': root + 'data/conversion_log.csv',
  					  'xml': root + 'data/xml/',
  					  'archive': root + 'data/archive/',
  					  'corpus': root + 'data/corpus/',
  					  'data': root + 'data/',
  					  'root': root,
  					  'lda': root + 'src/sporc/lda/',
  					  'doc2vec': root + 'src/sporc/doc2vec/'}

global_variables = {'absolute_filepaths': absolute_filepaths,
					'start': 2009,
					'end': 2019}

pickle.dump(global_variables, open(pickle_path, 'wb'))