#!/usr/bin/env python3
"""List all journals from _data/publications/refs.yml."""

import yaml
from collections import Counter

with open("../_data/publications/refs.yml") as f:
    data = yaml.safe_load(f)

entries = data.get("entries", {})

journals = Counter()
for key, entry in entries.items():
    journal = entry.get("journal")
    if journal:
        journals[journal] += 1

print(f"{'Journal':<60} {'Count':>5}")
print("-" * 66)
for journal, count in sorted(journals.items(), key=lambda x: -x[1]):
    print(f"{journal:<60} {count:>5}")

print(f"\nTotal unique journals: {len(journals)}")
print(f"Total entries with journal: {sum(journals.values())}")
print(f"Total entries: {len(entries)}")
