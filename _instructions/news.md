# How to Add News Entries

News entries are stored in `_data/news.yml`. Each entry is a YAML list item that appears on the website in chronological order.

## Required Fields

- **date**: Publication date in `"YYYY-MM-DD"` format (quoted string).
- **text**: The news text. Starts with an emoji indicating the category, followed by the description.

## Optional Fields

- **tag**: Categorizes the news entry. Known values:
  - `cv` - Career milestones, awards, positions, visits
  - `publication` - Published papers
  - `talk` - Presentations and seminars
  - `student` - Student defenses and achievements
- **links**: A list of URLs or local file paths related to the news item. Can include:
  - External URLs (e.g., `https://doi.org/...`)
  - Local images (e.g., `images/some_pictures/2025-SBAI1.jpeg`)
  - Local PDFs (e.g., `pdfs/slides/2023-PUCRio.pdf`)
  - Internal site pages (e.g., `./group`)
- **link**: A single URL (use `links` for multiple URLs).
- **photo**: Path to a photo associated with the entry (e.g., `images/some_pictures/2022-benzeliusaward.jpeg`).

## Emoji Conventions

Use an emoji at the start of the `text` field to indicate the type of news:

| Emoji | Meaning                           |
|-------|-----------------------------------|
| 📜    | New paper/publication             |
| 🏆    | Award or major achievement        |
| 🎬    | Talk or presentation              |
| 🎓    | Student thesis defense            |
| ✈️    | Research visit or travel          |
| 👨🏻‍🏫    | New position                      |
| 📝    | Announcement (e.g., hiring)       |

## Examples

### Paper publication with a single link

```yaml
- date: "2025-01-13"
  text: "📜 New paper at npj Digital Medicine. Evaluating AI-ECG in a longitudinal study."
  tag: publication
  links:
    - https://doi.org/10.1038/s41746-024-01428-7
```

### Paper publication with multiple links

```yaml
- date: "2024-06-25"
  text: "📜 Two new papers: npj Digital Medicine and Scientific Reports. AI-ECG for predicting electrolytes and cardiometabolic disease."
  tag: publication
  links:
    - https://www.nature.com/articles/s41746-024-01170-0
    - https://www.nature.com/articles/s41598-024-65223-w
```

### Career milestone

```yaml
- date: "2025-11-28"
  text: "🏆  I am now a Scilifelab Group leader."
  tag: cv
  links:
    - https://www.scilifelab.se/researchers/antonio-h-ribeiro/
```

### Talk with local image

```yaml
- date: "2025-11-20"
  text: "🎬  I participated as Faculty in the World Heart Federation emerging leaders programme. Teaching the next emerging leaders cohorts about AI."
  tag: cv
  links:
    - images/some_pictures/2025-emergingleaders.jpeg
```

### Student achievement

```yaml
- date: "2024-06-14"
  text: "🎓 Daniel Gedon successfully defended his PhD thesis. His thesis include publications on ICML, UAI, Scientific Reports and IEEE Signal Processing Letters. Next he is going to Tübingen University, Germany, as a PostDoc."
  tag: student
  links:
    - https://uu.diva-portal.org/smash/record.jsf?pid=diva2%3A1849417&dswid=9268
```

### Entry without links

```yaml
- date: "2024-11-25"
  text: "✈️ One month research visit to Francis Bach group at INRIA during November 2024."
  tag: cv
```

## Steps to Add a New Entry

1. Open `_data/news.yml`.
2. Add a new entry at the **top** of the file (newest entries first).
3. Fill in the required fields (`date`, `text`).
4. Add optional fields (`tag`, `links`, `photo`) as needed.
5. If linking to local files (images, PDFs), make sure those files exist in the repository.
