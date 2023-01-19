all: main.pdf

ROOT=..
TEMPLATE=template.tex
DATA=$(ROOT)/_data/
RENDER=$(ROOT)/scripts/render_from_template.py

main.pdf: main.tex main.bbl mypublicationlist.sty mycv.sty
	pdflatex -interaction=nonstopmode $<

main.bbl: main.bcf
	biber main

main.bcf: main.tex
	pdflatex -interaction=nonstopmode $<

mypublicationlist.sty: mypublicationlist_template.sty refs.bib
	python  $(RENDER) $< $(DATA) -o ./$@

main.tex: $(TEMPLATE) $(DATA)* $(RENDER)
	python $(RENDER) $< $(DATA) -o ./$@

.PHONY : clean
clean :
	rm *.log *.aux *.out *.bcf *.bbl *.blg *.log *.run.xml *.stderr *.stdout *.synctex.gz main.tex


# Maybe move somewhere else latter
short_cv.pdf: short_cv.tex short_cv.bbl mypublicationlist.sty mycv.sty
	pdflatex -interaction=nonstopmode short_cv.tex

short_cv.bbl: short_cv.bcf
	biber short_cv

short_cv.bcf: short_cv.tex
	pdflatex -interaction=nonstopmode short_cv.tex

short_cv.tex: short_cv_template.tex ../_data/* ../scripts/render_from_template.py
	python ../scripts/render_from_template.py short_cv_template.tex ../_data -o ./short_cv.tex