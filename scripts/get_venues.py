"""Extract and print all unique publication venues (journals/conferences)."""
import yaml
import argparse
from pathlib import Path

DEFAULT_REFS = Path(__file__).parent.parent / "_data" / "publications" / "refs.yml"
DEFAULT_CATEGORIES = Path(__file__).parent.parent / "_data" / "publications" / "categories.yml"


def load_yaml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    parser = argparse.ArgumentParser(description="List unique publication venues.")
    parser.add_argument("--refs", default=DEFAULT_REFS, help="Path to refs.yml")
    parser.add_argument("--categories", default=DEFAULT_CATEGORIES, help="Path to categories.yml")
    args = parser.parse_args()

    entries = load_yaml(args.refs)["entries"]
    categories = load_yaml(args.categories)

    # Build a mapping from paper id -> category name
    paper_category = {}
    for cat in categories:
        for paper_id in cat.get("papers", []):
            paper_category[paper_id] = cat["name"]

    # Collect venues per category
    venues_by_category = {}
    for paper_id, entry in entries.items():
        venue = entry.get("journal")
        if not venue:
            continue
        category = paper_category.get(paper_id, "Other")
        venues_by_category.setdefault(category, set()).add(venue)

    for category, venues in sorted(venues_by_category.items()):
        print(f"\n{category}:")
        for venue in sorted(venues):
            print(f"  {venue}")


if __name__ == "__main__":
    main()
