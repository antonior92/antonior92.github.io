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

$(NAME).sty: $(TEMPLATE)  $(DATA)* $(RENDER)
	python  $(RENDER) $(TEMPLATE) $(DATA) -o ./$@

