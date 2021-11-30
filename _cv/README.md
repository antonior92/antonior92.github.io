Compiling CV

```bash
python ../scripts/render_from_template.py template.tex ../_data -o ./main.tex
pdflatex main.tex -interaction=nonstopmode
biber main
pdflatex main.tex -interaction=nonstopmode
```