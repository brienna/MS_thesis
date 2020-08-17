# Data description:

- `dai_olah_le_triplets/` — — arXiv triplets used in Dai, Olah, and Le (2015). They encompass all categories, not only astrophysics.

- `archive/` — The original arXiv tars, downloaded from the Internet Archive.

- `xml/` — Full-text preprints, which were extracted from original tars, and then converted from TeX to XML.

- `corpus/` — Preprocessed abstracts and fulltexts.
	- `corpus/abstracts/` — Preprocessed abstracts. 
	- `corpus/fulltexts/` — Preprocessed fulltexts. 

- `metadata.csv` — Paper metadata. 

- `.gitignore` - Specifies large files not stored on GitHub, as well as unnecessary extras.

- `category_cooccurrences.rds` — Category cooccurrences table, used in notebooks/Generate_figures_in_R.ipynb

- `analogies.txt` — doc2vec analogies to test on the best-scoring model.

- `globals.p` — Global variables used in multiple notebooks, generated with `python src/set_globals.py`.


