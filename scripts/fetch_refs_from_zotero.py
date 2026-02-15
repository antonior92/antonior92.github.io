"""Fetch refs.bib from the Zotero Web API (My Publications)."""

import argparse
import sys
from urllib.request import urlopen
from urllib.error import URLError

USER_ID = "4218406"
API_URL = (
    f"https://api.zotero.org/users/{USER_ID}/publications/items"
    "?format=bibtex&limit=100"
)


def main():
    parser = argparse.ArgumentParser(
        description="Fetch BibTeX from the Zotero Web API."
    )
    parser.add_argument(
        "-o", "--output", default="refs.bib",
        help="Output file path (default: refs.bib)",
    )
    args = parser.parse_args()

    try:
        response = urlopen(API_URL)
    except URLError as e:
        print(f"Error: Could not fetch from Zotero API.\n{e}", file=sys.stderr)
        sys.exit(1)

    data = response.read().decode("utf-8")

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(data)

    print(f"Wrote {len(data)} bytes to {args.output}")


if __name__ == "__main__":
    main()
