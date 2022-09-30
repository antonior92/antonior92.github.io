all: main.pdf

main.pdf: main.tex main.bbl mypublicationlist.sty mycv.sty
	pdflatex -interaction=nonstopmode main.tex

main.bbl: main.bcf
	biber main

main.bcf: main.tex
	pdflatex -interaction=nonstopmode main.tex

mypublicationlist.sty: mypublicationlist_template.sty
	python ../scripts/render_from_template.py mypublicationlist_template.sty ../_data -o ./mypublicationlist.sty

main.tex: template.tex ../_data/* ../scripts/render_from_template.py
	python ../scripts/render_from_template.py template.tex ../_data -o ./main.tex

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