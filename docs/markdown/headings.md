# 2. Headings & Document Structure

Headings describe the outline of a page. In this lesson you will build a heading
hierarchy and see how MkDocs turns it into navigation.

## Write headings

Put one or more `#` characters at the start of a line, followed by a space:

```markdown
# Analysis guide

A short introduction.

## Prepare the data

Describe the preparation steps.

### Check the input files

Explain one part of preparation.

## Run the analysis

Describe the next major stage.
```

`#` is level 1, `##` is level 2, and `###` is level 3. Markdown supports levels
through `######`. Use one level-1 heading for the page title, level 2 for main
sections, and level 3 for their subsections. Avoid jumping from level 1 straight
to level 3: levels express relationships rather than a preferred font size.

## See a hierarchy

This section and the subsection below are live headings. Compare their nesting
in this page's table of contents.

### A subsection of “See a hierarchy”

This text belongs to the subsection. The next level-2 heading starts a new main
section. Keep blank lines around headings so the source stays easy to scan.

## Understand automatic navigation

MkDocs uses two related structures:

- **Site navigation** links between files. Without an explicit `nav` setting,
  MkDocs discovers Markdown pages. This project uses `nav` in `mkdocs.yaml` to
  choose their labels, grouping, and order.
- **The page table of contents** links to headings inside a file. The `toc`
  extension creates heading IDs, and Material displays the outline. On small
  screens, navigation is accessed through the theme's menu controls.

For example, this configuration links a menu entry to a file under `docs/`:

```yaml
nav:
  - Markdown tutorials:
      - Headings: markdown/headings.md
```

The navigation label can differ from the page title. You do not need to list
every `##` heading in `nav`.

## Link directly to a section

The heading `## Write headings` becomes the anchor `#write-headings` here:

```markdown
[Return to the syntax](#write-headings)
```

[Return to the syntax](#write-headings).

For simple heading names, anchors use lower-case words with hyphens instead of
spaces. This project adds clickable heading permalinks with:

```yaml
markdown_extensions:
  - toc:
      permalink: true
```

Use the heading's permalink to copy its actual anchor, especially for titles
containing punctuation or repeated titles. Renaming a heading can break links.

## Try it

Write a page called “Experiment guide” with one page title, two main sections,
and a subsection under the first section. Preview it, inspect its table of
contents, and add a link to the second section.

**Next:** [Text Formatting](text-formatting.md).
