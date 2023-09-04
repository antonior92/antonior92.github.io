ROOT=..
NAME=publicationlist
TEMPLATE=$(NAME)_template
DATA=$(ROOT)/_data/
RENDER=$(ROOT)/scripts/render_from_template.py


all: $(NAME).pdf

$(NAME).pdf: $(NAME).tex $(NAME).bbl $(NAME).sty ../_cv/mycv.sty
	pdflatex -interaction=nonstopmode $<

$(NAME).bbl: $(NAME).bcf
	biber $(NAME)

$(NAME).bcf: $(NAME).tex
	pdflatex -interaction=nonstopmode $<

$(NAME).sty: $(TEMPLATE) ../_publicationlist/refs.bib
	python  $(RENDER) $< $(DATA) -o ./$@

$(NAME).tex:  $(DATA)* $(RENDER)
	python $(RENDER) $< $(DATA) -o ./$@
