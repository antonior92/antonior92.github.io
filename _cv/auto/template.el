(TeX-add-style-hook
 "template"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "10pt" "letterpaper")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("geometry" "left=1cm" "top=1.2cm" "right=1cm" "bottom=1.2cm") ("parskip" "parfill") ("biblatex" "sorting=ydnt" "maxbibnames=99" "style=ieee")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "hyperref"
    "xcolor"
    "geometry"
    "parskip"
    "array"
    "biblatex")
   (LaTeX-add-bibliographies
    "refs"))
 :latex)

