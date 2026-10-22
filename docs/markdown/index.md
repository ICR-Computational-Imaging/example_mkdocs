# Markdown tutorials

Markdown is plain text with formatting markers. MkDocs turns your Markdown files
into a documentation website, and the Material theme adds navigation, search,
and support for richer content.

## Choose a lesson

The lesson numbers follow the supplied course sequence, starting at 2.

| Lesson | What you will learn |
| :--- | :--- |
| [1. Headings & Document Structure](headings.md) | Organise a page and understand automatic navigation. |
| [2. Text Formatting](text-formatting.md) | Add emphasis, code spans, and horizontal rules. |
| [3. Lists & Task Lists](lists.md) | Write steps, nested lists, and checklists. |
| [4. Links & Images](links-and-images.md) | Connect pages and embed images using relative paths. |
| [5. Code Blocks & Syntax Highlighting](code-blocks.md) | Present readable, copyable code. |
| [6. Tables](tables.md) | Compare options and align structured information. |
| [7. Mathematical Equations](mathematics.md) | Write LaTeX equations and configure MathJax. |
| [8. Admonitions & Callouts](admonitions.md) | Add notes, warnings, tips, and collapsible explanations. |
| [9. Documentation with mkdocstrings](mkdocstrings.md) | Generate API reference material from Python docstrings. |
| [10. Advanced Features & MkDocs Integration](advanced.md) | Combine diagrams, tabs, cross-references, and extensions. |

## Work through the examples

Each lesson explains the syntax, shows a result, and ends with an exercise.
Create a scratch page such as `docs/practice.md` and paste examples into it.
MkDocs builds Markdown pages even if they are absent from `nav`; visit
`/practice/` in the local preview, or add the page to `nav` as shown in lesson 10.

Start the preview from the repository root:

```bash
uv sync
uv run mkdocs serve
```

## Understand the renderer

Headings, emphasis, links, and lists use ordinary Markdown syntax. Task lists,
strikethrough, maths, admonitions, diagrams, and tabs need extensions or browser
scripts. These are already configured in this project's `mkdocs.yaml`; the lessons
explain their setup. Other Markdown viewers may display these features differently.

**Next:** [Headings & Document Structure](headings.md).
