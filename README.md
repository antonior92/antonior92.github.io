# My personal webpage

# Running locally

My favorite way to run this page locally is to just use the docker image
from [Starefossen/docker-github-pages](https://github.com/Starefossen/docker-github-pages).

That is just run:
```
git clone https://github.com/github/pages-gem.git
cd pages-gem
make image
cd ..
rm -rf pages-gem


docker run --rm -it \
    -p 4000:4000 \
    -v ${PWD}:/src/site \
    gh-pages \
    sh -c "bundle install && bundle exec jekyll serve -H 0.0.0.0 -P 4000"
```
Your Jekyll page will be available on `http://localhost:4000`.

OBS: If the port 4000 is occupied you might find out which process by using: `lsof -i:4000`.

# Generating cv
Load cv as a submodule:
```
git submodule init 
git submodule update
```

Generate pdf using pdflatex: 
```
cd CV
mkdir out
pdflatex -output-dir=out -interaction=nonstopmode main.tex
biber --input-directory out --output-directory out main
pdflatex -output-dir=out -interaction=nonstopmode main.tex
pdflatex -output-dir=out -interaction=nonstopmode main.tex
mv out/main.pdf ../pdfs/cv.pdf
```