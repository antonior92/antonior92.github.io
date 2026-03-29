# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a Jekyll-based academic personal website with integrated LaTeX CV and publication list generation. Content is data-driven: all structured information lives in `_data/` as YAML files, which are consumed both by Jekyll (for the website) and by Python+Liquid templating scripts (for PDF generation).

## Commands

### Run website locally

First-time setup (build Docker image):
```bash
git clone https://github.com/github/pages-gem.git
cd pages-gem && make image && cd .. && rm -rf pages-gem
```

Serve locally at `http://localhost:4000`:
```bash
docker run --rm -it \
    -p 4000:4000 \
    -v ${PWD}:/src/site \
    gh-pages \
    sh -c "bundle install && bundle exec jekyll serve -H 0.0.0.0 -P 4000"
```

### Generate CV PDF

```bash
cd _cv
make          # renders template.tex → main.tex, then compiles to main.pdf
make clean    # remove build artifacts
```

### Generate Publication List PDF

```bash
cd _publicationlist
make          # renders template → publicationlist.sty, compiles publicationlist.pdf
make fetch    # fetch references from Zotero into refs.bib
make clean
```

### Template rendering (manual)

```bash
python scripts/render_from_template.py <template_file> _data/ -o <output_file>
```

## Architecture

### Data layer (`_data/`)

All content is stored as YAML. The website and PDFs are generated from the same data sources:

- `_data/*.yml` — top-level entries: `news.yml`, `academicpositions.yml`, `education.yml`, `awards.yml`, `talks.yml`, `teaching.yml`, `grants.yml`, etc.
- `_data/publications/` — publication data split into: `refs.yml` (metadata), `links.yml` (URLs), `categories.yml` (grouping), `notes.yml`, `venues.yml`
- `_data/professional/` — `journalreviews.yml`, `conferencereviews.yml`, `others.yml`
- `_data/supervision/` — supervision data

### Website layer (Jekyll)

- `_pages/*.html` — page content using Liquid templating against `site.data.*`
- `_layouts/default.html` — main layout with sidebar, MathJax, navigation
- `_config.yml` — Jekyll configuration; uses `jekyll-scholar` for bibliography

### PDF generation layer

`scripts/render_from_template.py` reads YAML from `_data/` recursively and builds a nested data structure matching the directory hierarchy. It renders Liquid templates — `_cv/template.tex` becomes `_cv/main.tex`, and `_publicationlist/publicationlist_template` becomes `_publicationlist/publicationlist.sty`.

The CV (`_cv/`) uses only `pdflatex` (no biber). The publication list (`_publicationlist/`) uses `pdflatex` + `bibtex` with `refs.bib`.

### Skills / slash commands

Two custom skills are registered for common tasks:
- `/add-publication` — adds a new publication entry
- `/fill-in-news` — adds a news entry to `_data/news.yml`
