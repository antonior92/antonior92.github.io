all: main.pdf

ROOT=..
TEMPLATE=template.tex
DATA=$(ROOT)/_data/
RENDER=$(ROOT)/scripts/render_from_template.py

main.pdf: main.tex mycv.sty
	pdflatex -interaction=nonstopmode $<

main.tex: $(TEMPLATE) $(DATA)* $(RENDER)
	python $(RENDER) $< $(DATA) -o ./$@

.PHONY : clean
clean :
	rm *.log *.aux *.out *.bcf *.bbl *.blg *.log *.run.xml *.stderr *.stdout *.synctex.gz main.tex
