#!/usr/bin/env python3
"""Find publications missing from categories.yml and report duplicates."""

import argparse
import yaml

parser = argparse.ArgumentParser(description="Check which refs are missing from categories.yml.")
parser.add_argument("refs", nargs="?", default="../_data/publications/refs.yml")
parser.add_argument("categories", nargs="?", default="../_data/publications/categories.yml")
args = parser.parse_args()

with open(args.refs) as f:
    refs = yaml.safe_load(f)
with open(args.categories) as f:
    cats = yaml.safe_load(f)

all_keys = set(refs.get("entries", {}).keys())

cat_keys = []
for cat in cats:
    cat_keys.extend(cat.get("papers", []))

seen = set()
dupes = []
for k in cat_keys:
    if k in seen:
        dupes.append(k)
    seen.add(k)

missing = all_keys - set(cat_keys)

if missing:
    print("Missing from categories.yml:")
    for k in sorted(missing):
        entry = refs["entries"][k]
        venue = entry.get("journal", entry.get("booktitle", "(no venue)"))
        entry_type = entry.get("type", "article")
        print(f"  {k} [{entry_type}]: {venue}")
else:
    print("All entries are accounted for in categories.yml.")

if dupes:
    print(f"\nDuplicates in categories.yml: {dupes}")
else:
    print("\nNo duplicates.")
