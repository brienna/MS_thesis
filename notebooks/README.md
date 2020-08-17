## Notebook description: 

`Download_paper_metadata.ipynb` — Downloads arXiv paper metadata to `./data/docs_metadata.csv`, or updates the file if it already exists.

`Scrape_archive.org.ipynb` — Scrapes archive.org for tarred arXiv papers, downloading the tars to `./data/docs_archived/`

`Extract_and_convert_papers.ipynb` — Extracts papers from the tars, and converts them from TEX to XML, to simplify downstream parsing. Adds `has_xml` column to `metadata.csv`. (Notebook is quite messy.)

`Build_corpus.ipynb` — Explores paper metadata in `./data/docs_metadata.csv`, determines our desired time range and edits the file, specifying whether each paper falls within this time range, adding `in_range` column to metadata. We also filter based on results of fulltext conversion. 

`Explore_corpus.ipynb` — Visualizes various corpus attributes.

`Preprocess_corpus.ipynb` — Parses XML fulltexts and preprocesses abstracts and fulltexts.

`Generate_evaluation_triplets` — Generates evaluation triplets.

`Analyze_models` — Analyzes results from doc2vec and LDA training.

`Generate_figures_in_R` — Generates certain visualizations in R.

`Scratch` — Temporary workbook.







