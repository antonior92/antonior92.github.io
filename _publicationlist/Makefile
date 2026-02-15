ROOT=..
NAME=publicationlist
REFS=refs
TEMPLATE=$(NAME)_template
DATA=$(ROOT)/_data/
RENDER=$(ROOT)/scripts/render_from_template.py
CLEAN=$(ROOT)/scripts/clean_latex_yaml.py
REPLACE=$(ROOT)/scripts/replace_journal_names.py

all: $(NAME).pdf $(REFS).yml

$(NAME).pdf: $(NAME).tex $(NAME).sty $(NAME).bbl $(NAME).sty ../_cv/mycv.sty
	pdflatex -interaction=nonstopmode $<

$(NAME).bbl: $(NAME).bcf $(REFS).bib
	bibtex $(NAME)

$(NAME).bcf: $(NAME).tex $(NAME).sty
	pdflatex -interaction=nonstopmode $<

$(NAME).sty: $(TEMPLATE) $(DATA)/publications/* $(RENDER)
	python  $(RENDER) $(TEMPLATE) $(DATA) -o ./$@

$(REFS).yml:  $(REFS).bib $(CLEAN) $(REPLACE)
	pybtex-convert refs.bib refs.yaml
	mv refs.yaml refs.yml
	python $(CLEAN) refs.yml refs.yml
	python $(REPLACE) refs.yml refs.yml

fetch:
	python $(ROOT)/scripts/fetch_refs_from_zotero.py -o $(REFS).bib

.PHONY : clean fetch
clean :
	rm *.log *.aux *.out *.bcf *.bbl *blx.bib *.blg *.log *.run.xml *.stderr *.stdout *.synctex.gz publicationlist.sty *.pdf
