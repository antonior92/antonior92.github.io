import yaml
import re
import sys

# Define replacements
journal_replacements = {
    r"IEEE Conference on Decision and Control \(CDC\)": "CDC",
    r"International Conference on Artificial Intelligence and Statistics \(AISTATS\)": "AISTATS",
    r"Advances in Neural Information Processing Systems": "NeurIPS",
    r"IFAC Workshop on Automatic Control in Offshore Oil and Gas Production": "IFAC Oil and Gas",
    r"NeurIPS 2024 Workshop on Scientific Methods for Understanding Deep Learning": "NeurIPS Workshop Sci4DL",
    r"Machine Learning for Health (ML4H) Workshop at NeurIPS": "NeurIPS Workshop ML4H",
    r".*\(([^()]+)\)\s*$": r"\1"
}

def replace_journal_name(journal):
    for pattern, replacement in journal_replacements.items():
        journal = re.sub(pattern, replacement, journal)
    return journal

def process_entry(entry):
    if isinstance(entry, dict):
        if 'journal' in entry and isinstance(entry['journal'], str):
            entry['journal'] = replace_journal_name(entry['journal'])
        for k, v in entry.items():
            entry[k] = process_entry(v)
    elif isinstance(entry, list):
        entry = [process_entry(e) for e in entry]
    return entry

def main(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    data['entries'] = {k: process_entry(v) for k, v in data['entries'].items()}

    with open(output_path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python replace_journal_names.py input.yml output.yml")
    else:
        main(sys.argv[1], sys.argv[2])