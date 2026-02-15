"""Fetch refs.bib from the Zotero Web API (My Publications).

Unicode characters are converted to LaTeX escapes so that
BibTeX8 (which cannot handle raw UTF-8) processes the file correctly.
"""

import argparse
import re
import sys
from urllib.request import urlopen, Request
from urllib.error import URLError

USER_ID = "4218406"
BASE_URL = (
    f"https://api.zotero.org/users/{USER_ID}/publications/items"
    "?format=bibtex&limit=100"
)

# Map of Unicode characters to LaTeX equivalents.
UNICODE_TO_LATEX = {
    "\u00A0": "~",            # non-breaking space
    "\u00A9": r"\textcopyright{}",
    "\u00B1": r"$\pm$",       # ±
    "\u00B7": r"\textperiodcentered{}",  # ·
    "\u00C0": r"\`{A}",
    "\u00C1": r"\'{A}",
    "\u00C2": r"\^{A}",
    "\u00C3": r"\~{A}",
    "\u00C4": r'\"{A}',
    "\u00C5": r"\r{A}",
    "\u00C7": r"\c{C}",
    "\u00C8": r"\`{E}",
    "\u00C9": r"\'{E}",
    "\u00CA": r"\^{E}",
    "\u00CB": r'\"{E}',
    "\u00CD": r"\'{I}",
    "\u00CE": r"\^{I}",
    "\u00D1": r"\~{N}",
    "\u00D3": r"\'{O}",
    "\u00D4": r"\^{O}",
    "\u00D6": r'\"{O}',
    "\u00D8": r"\O{}",
    "\u00DA": r"\'{U}",
    "\u00DC": r'\"{U}',
    "\u00DF": r"\ss{}",
    "\u00E0": r"\`{a}",
    "\u00E1": r"\'{a}",
    "\u00E2": r"\^{a}",
    "\u00E3": r"\~{a}",
    "\u00E4": r'\"{a}',
    "\u00E5": r"\r{a}",
    "\u00E6": r"\ae{}",
    "\u00E7": r"\c{c}",
    "\u00E8": r"\`{e}",
    "\u00E9": r"\'{e}",
    "\u00EA": r"\^{e}",
    "\u00EB": r'\"{e}',
    "\u00ED": r"\'{i}",
    "\u00EE": r"\^{i}",
    "\u00EF": r'\"{i}',
    "\u00F1": r"\~{n}",
    "\u00F2": r"\`{o}",
    "\u00F3": r"\'{o}",
    "\u00F4": r"\^{o}",
    "\u00F5": r"\~{o}",
    "\u00F6": r'\"{o}',
    "\u00F8": r"\o{}",
    "\u00F9": r"\`{u}",
    "\u00FA": r"\'{u}",
    "\u00FB": r"\^{u}",
    "\u00FC": r'\"{u}',
    "\u0130": r"\.{I}",       # İ (capital I with dot above)
    "\u015E": r"\c{S}",       # Ş
    "\u015F": r"\c{s}",       # ş
    "\u0131": r"{\i}",        # ı (dotless i)
    "\u2013": "--",            # en-dash
    "\u2014": "---",           # em-dash
    "\u00FD": r"\'{y}",       # ý
    "\u0161": r"\v{s}",       # š
    "\u2008": " ",             # punctuation space
    "\u2009": " ",             # thin space
    "\u2013": "--",            # en-dash
    "\u2014": "---",           # em-dash
    "\u2018": "`",             # left single quote
    "\u2019": "'",             # right single quote
    "\u201C": "``",            # left double quote
    "\u201D": "''",            # right double quote
    "\u2032": "'",             # prime (′)
    "\u202F": " ",             # narrow no-break space
    "\u2265": r"$\geq$",      # ≥
    "\uFB01": "fi",            # ﬁ ligature
    "\uFB02": "fl",            # ﬂ ligature
}


def unicode_to_latex(text):
    """Replace non-ASCII characters with LaTeX equivalents."""
    def replace_char(m):
        ch = m.group()
        return UNICODE_TO_LATEX.get(ch, ch)

    # Build pattern from known mappings
    known = re.escape("".join(UNICODE_TO_LATEX.keys()))
    text = re.sub(f"[{known}]", replace_char, text)

    # Warn about any remaining non-ASCII characters
    for m in re.finditer(r"[^\x00-\x7f]", text):
        ch = m.group()
        pos = m.start()
        context = text[max(0, pos - 20):pos + 20]
        print(
            f"Warning: unmapped U+{ord(ch):04X} ({ch}) near: ...{context}...",
            file=sys.stderr,
        )

    return text


def fetch_all_bibtex():
    """Fetch all BibTeX entries, paginating if needed."""
    chunks = []
    start = 0

    while True:
        url = f"{BASE_URL}&start={start}"
        try:
            resp = urlopen(Request(url))
        except URLError as e:
            print(f"Error: Could not fetch from Zotero API.\n{e}", file=sys.stderr)
            sys.exit(1)

        total = int(resp.headers.get("Total-Results", 0))
        chunk = resp.read().decode("utf-8")
        if chunk.strip():
            chunks.append(chunk)

        start += 100
        if start >= total:
            break

    return "\n".join(chunks)


def main():
    parser = argparse.ArgumentParser(
        description="Fetch BibTeX from the Zotero Web API."
    )
    parser.add_argument(
        "-o", "--output", default="refs.bib",
        help="Output file path (default: refs.bib)",
    )
    args = parser.parse_args()

    data = fetch_all_bibtex()
    data = unicode_to_latex(data)

    with open(args.output, "w", encoding="ascii", errors="backslashreplace") as f:
        f.write(data)

    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
