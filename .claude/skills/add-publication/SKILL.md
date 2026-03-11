For add a new publication.

1. Run ``make fectch`` from inside _publicationlist. This will update "refs.bib" with the latest publications I have in Zotero
2. Run ``make`` from inside _publicationlist. This will update "refs.yml" from "refs.bib".
3. Run ``python scripts/list_journals.py``. This will list all journals I have published in, and the number of publications in each journal.
4. If the journal of the new publication is not in the list, add it to "_data/publications/venues.yml". You can copy the format of the existing entries. Make sure to include the "impact_factor" field, "conference", "journal". Look at previous information in venues.yml to see how to fill it in. You can find the impact factor of the journal by searching for it together with "JCR impact factor" on google.
5. Read ``publication/categories.yml`` and see it all the publications are in the list or not. If some publication is not there. Check in venues, and add it to the list either as "journal" or "conference". Dont add workshops.
6. Check if there is news and add the publication to the news if it is not there. You can check the skill fill in news items to see how to add it.

