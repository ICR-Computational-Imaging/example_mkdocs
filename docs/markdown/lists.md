# 4. Lists & Task Lists

Use bullets for related items, ordered lists for steps, and task lists for
progress. Indentation keeps nested content inside its parent item.

## Write a bullet list

Start each item with `-` and a space. Leave a blank line before the list:

```markdown
Required files:

- Input images
- Configuration file
- Output directory
```

Required files:

- Input images
- Configuration file
- Output directory

`*` and `+` also work as bullets. Choose one style and use it consistently.

## Write an ordered list

Use numbers followed by a full stop for steps where order matters:

```markdown
1. Prepare the input files.
2. Run the analysis.
3. Inspect the output.
```

1. Prepare the input files.
2. Run the analysis.
3. Inspect the output.

You can also start every source item with `1.`; the renderer numbers them in
sequence. Explicit numbers often make the source easier to read.

## Nest lists and paragraphs

For Python Markdown, the renderer used by MkDocs, indent nested lists by **four
spaces**. Continuation paragraphs also need four spaces and a preceding blank
line. Other renderers may accept different indentation.

```markdown
1. Prepare the data.

    - Check file names.
    - Confirm image dimensions.

    Keep a copy of the original files before making changes.

2. Run the analysis.
```

1. Prepare the data.

    - Check file names.
    - Confirm image dimensions.

    Keep a copy of the original files before making changes.

2. Run the analysis.

Use spaces rather than tabs. If a child item appears at the top level, check its
indentation and the blank line before it.

## Track progress with task lists

Use `[ ]` for incomplete tasks and `[x]` for completed tasks:

```markdown
- [x] Create the documentation folder.
- [x] Add the first tutorial.
- [ ] Review the rendered website.
```

- [x] Create the documentation folder.
- [x] Add the first tutorial.
- [ ] Review the rendered website.

In this configuration the checkboxes are disabled in the browser. Edit `[ ]` to
`[x]` in the Markdown source to update the saved status.

Task lists require an extension. This project uses the
[Material task-list configuration](https://squidfunk.github.io/mkdocs-material/reference/lists/#configuration):

```yaml
markdown_extensions:
  - pymdownx.tasklist:
      custom_checkbox: true
```

## Try it

Create an ordered three-step publishing workflow. Add two nested bullets under
the first step and a separate task list showing your progress. Check that the
nested bullets stay inside their parent item in the preview.

**Next:** [Links & Images](links-and-images.md).
