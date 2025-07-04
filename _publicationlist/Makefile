ROOT=..
NAME=publicationlist
TEMPLATE=$(NAME)_template
DATA=$(ROOT)/_data/
RENDER=$(ROOT)/scripts/render_from_template.py


all: $(NAME).pdf

$(NAME).pdf: $(NAME).tex $(NAME).sty $(NAME).bbl $(NAME).sty ../_cv/mycv.sty
	pdflatex -interaction=nonstopmode $<

$(NAME).bbl: $(NAME).bcf refs.bib
	bibtex $(NAME)

$(NAME).bcf: $(NAME).tex $(NAME).sty
	pdflatex -interaction=nonstopmode $<

$(NAME).sty: $(TEMPLATE) $(DATA)/publications/* $(RENDER)
	python  $(RENDER) $(TEMPLATE) $(DATA) -o ./$@



.PHONY : clean
clean :
	rm *.log *.aux *.out *.bcf *.bbl *blx.bib *.blg *.log *.run.xml *.stderr *.stdout *.synctex.gz publicationlist.sty *.pdf
