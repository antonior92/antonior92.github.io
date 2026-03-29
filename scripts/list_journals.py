#!/usr/bin/env python3
"""List all journals from _data/publications/refs.yml."""

import argparse
import yaml
from collections import Counter

parser = argparse.ArgumentParser(description="List all journals from a refs.yml file.")
parser.add_argument("refs", nargs="?", default="../_data/publications/refs.yml")
args = parser.parse_args()

with open(args.refs) as f:
    data = yaml.safe_load(f)

entries = data.get("entries", {})

journals = Counter()
journal_keys = {}
for key, entry in entries.items():
    journal = entry.get("journal")
    if journal:
        journals[journal] += 1
        journal_keys.setdefault(journal, []).append(key)

print(f"{'Journal':<60} {'Count':>5}  {'Citations'}")
print("-" * 100)
for journal, count in sorted(journals.items(), key=lambda x: -x[1]):
    keys = ", ".join(journal_keys[journal])
    print(f"{journal:<60} {count:>5}  {keys}")

print(f"\nTotal unique journals: {len(journals)}")
print(f"Total entries with journal: {sum(journals.values())}")
print(f"Total entries: {len(entries)}")
