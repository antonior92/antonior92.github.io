all: main.pdf

main.pdf: main.tex main.bbl
	pdflatex -interaction=nonstopmode main.tex

main.bbl: main.bcf
	biber main

main.bcf: main.tex
	pdflatex -interaction=nonstopmode main.tex

main.tex: template.tex ../_data/* ../scripts/render_from_template.py
	python ../scripts/render_from_template.py template.tex ../_data -o ./main.tex

.PHONY : clean
clean :
	rm *.log *.aux *.out *.bcf *.bbl *.blg *.log *.run.xml *.stderr *.stdout *.synctex.gz main.tex