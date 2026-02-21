"""Extract and print all unique publication venues from a BibTeX file."""
import re
import argparse
from pathlib import Path

DEFAULT_REFS = Path(__file__).parent.parent / "_publicationlist" / "refs.bib"


def extract_journals(bib_path):
    text = Path(bib_path).read_text(encoding="utf-8")
    # Match: journal = {value} or journal = "value"
    pattern = re.compile(r'^\s*journal\s*=\s*[{"](.*?)[}"],?\s*$', re.MULTILINE)
    return {m.group(1).strip() for m in pattern.finditer(text)}


def main():
    parser = argparse.ArgumentParser(description="List unique publication venues from a BibTeX file.")
    parser.add_argument("--refs", default=DEFAULT_REFS, help="Path to refs.bib")
    args = parser.parse_args()

    venues = extract_journals(args.refs)
    for venue in sorted(venues):
        print(venue)


if __name__ == "__main__":
    main()
