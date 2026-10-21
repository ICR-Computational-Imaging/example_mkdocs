# 7. Tables

Tables make related facts easy to compare. Learn to define columns, align their
content, and choose information suited to a table.

## Create a table

Separate columns with `|` and put a separator row immediately below the header:

```markdown
| File | Purpose |
| --- | --- |
| `mkdocs.yaml` | Site configuration |
| `docs/index.md` | Home page |
| `docs/assets/logo.svg` | Project logo |
```

| File | Purpose |
| --- | --- |
| `mkdocs.yaml` | Site configuration |
| `docs/index.md` | Home page |
| `docs/assets/logo.svg` | Project logo |

The header and separator must define the same number of columns. Use at least
three hyphens per separator cell. Spaces help source readability, but columns
need not line up perfectly in the editor. Leave blank lines around the table.

## Align columns

Use colons in the separator row:

```markdown
| Item | Status | Count |
| :--- | :---: | ---: |
| Pages drafted | Ready | 9 |
| Reviews pending | Open | 2 |
```

| Item | Status | Count |
| :--- | :---: | ---: |
| Pages drafted | Ready | 9 |
| Reviews pending | Open | 2 |

`:---` aligns left, `:---:` centres, and `---:` aligns right. Right alignment
helps compare numbers. Include units in headers, such as `Duration (s)`.

## Compare options

Use a table when the same questions apply to every option:

| Format | Best suited to | Main limitation |
| :--- | :--- | :--- |
| Paragraph | Explaining a concept | Hard to compare many attributes |
| Bullet list | Listing related points | Few explicit relationships between columns |
| Table | Comparing consistent attributes | Long prose is difficult to scan |

Keep cells short. Use [lists](lists.md) for steps and ordinary sections for long
explanations. A Markdown table does not calculate totals or sort itself.

## Format cell contents

Cells can contain **bold**, inline `code`, and [links](links-and-images.md).
Escape a literal pipe so it does not start another column:

```markdown
| Symbol | Meaning |
| --- | --- |
| A \| B | A or B |
```

| Symbol | Meaning |
| --- | --- |
| A \| B | A or B |

Keep each row on one source line. Merged cells, complex blocks, and
multi-paragraph cells are outside the scope of ordinary Markdown tables.

## Enable tables

This project explicitly enables Python Markdown's table extension:

```yaml
markdown_extensions:
  - tables
```

## Try it

Compare three output formats using columns for extension, typical use, and
example size in kilobytes. Left-align descriptions, right-align sizes, and put
a link in one cell. Verify the result in the preview.

**Next:** [Mathematical Equations](mathematics.md).
