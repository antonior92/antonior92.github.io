
PH="scripts/"
pybtex-convert _publicationlist/refs.bib _data/publications/refs.yaml
python $PH/clean_latex_yaml.py _data/publications/refs.yaml  _data/publications/refs.yml
python $PH/replace_journal_names.py  _data/publications/refs.yml  _data/publications/refs.yml