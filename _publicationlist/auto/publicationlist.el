(TeX-add-style-hook
 "publicationlist"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("biblatex" "sorting=none" "maxbibnames=99" "mincitenames=99" "maxcitenames=99" "style=numeric" "backend=bibtex" "defernumbers=true" "isbn=false" "url=false" "eprint=false" "giveninits=true")))
   (TeX-run-style-hooks
    "biblatex")
   (TeX-add-symbols
    '("mkboldifhashinlist" 1)
    "nhblx"
    "addboldnames"
    "resetboldnames"
    "printmypublications"))
 :latex)

