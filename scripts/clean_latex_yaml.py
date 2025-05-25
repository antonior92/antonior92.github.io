import yaml
import re
import sys
import codecs
from typing import Any
import latexcodec  # needed for codec registration


def latex_to_unicode(s: str) -> str:
    """Convert LaTeX-encoded string to Unicode."""
    if not isinstance(s, str):
        return s
    s = re.sub(r"\{\{(.*?)\}\}", r"\1", s)  # Remove double braces like {{text}}
    s = re.sub(r"\{(.*?)\}", r"\1", s)  # Remove single braces like {text}
    return codecs.decode(s.encode('utf-8'), 'latex+utf-8')

def clean_entry(entry: Any) -> Any:
    """Recursively clean YAML entries by converting LaTeX strings to Unicode."""
    if isinstance(entry, dict):
        return {k: clean_entry(v) for k, v in entry.items()}
    elif isinstance(entry, list):
        return [clean_entry(item) for item in entry]
    elif isinstance(entry, str):
        return latex_to_unicode(entry)
    else:
        return entry

def main(input_file: str, output_file: str) -> None:
    with open(input_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    cleaned_data = {
        'entries': {k: clean_entry(v) for k, v in data.get('entries', {}).items()}
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        yaml.dump(cleaned_data, f, allow_unicode=True, sort_keys=False)

    print(f"Cleaned file saved to: {output_file}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python clean_latex_yaml.py input.yml output.yml")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
