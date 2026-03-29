For add a new publication.

1. Save current state: run `python scripts/list_journals.py` from the repo root and save output to `journals.txt`.
2. Fetch latest refs from Zotero: run `make fetch` from inside `_publicationlist`. This updates `refs.bib`.
3. Sync refs to data: run `python scripts/check_new_refs.py` from `scripts/`. This compares `_publicationlist/refs.yml` with `_data/publications/refs.yml` and shows new entries. If there are new entries, re-run with `--sync` to copy the updated file.
4. Run `python scripts/list_journals.py` again and diff with `journals.txt`.
   a. If no diff, there are no new publications — stop here.
   b. If there are changes, continue.
5. If the journal/conference of the new publication is not already in `_data/publications/venues.yml`, add it. Copy the format of existing entries. Include `impact_factor`, `type` (journal or conference), and `tag`. Find the JCR impact factor by searching `"<journal name>" JCR impact factor`.
6. Rebuild refs.yml: run `make refs.yml` from inside `_publicationlist`. This regenerates `_publicationlist/refs.yml` from `refs.bib`.
7. Run `python scripts/check_categories.py` from `scripts/`. This shows entries missing from `_data/publications/categories.yml` and any duplicates. Add missing journal and conference papers to the correct category. Do not add workshops, theses, or dissertations.
8. Check if the new publication has a news entry in `_data/news.yml`. If not, use the `fill-in-news` skill to add one.
