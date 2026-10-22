# 9. Admonitions & Callouts

Callouts draw attention to supporting information and consequences. Material
styles these blocks as notes, warnings, tips, and other admonition types.

## Add a note

Start with `!!!`, a type, and an optional title in double quotes. Indent the
body by four spaces:

```markdown
!!! note "Before you start"

    Run commands from the repository root.
```

!!! note "Before you start"

    Run commands from the repository root.

If you omit the title, the type supplies a default title. Text without the
four-space indentation falls outside the callout.

## Choose a useful type

Match the type to what readers should do with the information:

```markdown
!!! warning "Check the destination"

    An export may overwrite a file with the same name.

!!! tip "Preview while editing"

    Keep `uv run mkdocs serve` running to see changes after saving.
```

!!! warning "Check the destination"

    An export may overwrite a file with the same name.

!!! tip "Preview while editing"

    Keep `uv run mkdocs serve` running to see changes after saving.

Use notes for supporting information, tips for useful shortcuts, and warnings
for consequences to consider before acting. Too many callouts interrupt reading.

## Include lists and code

Indent all content belonging to the admonition, including fences:

````markdown
!!! example "Build checklist"

    1. Save your Markdown files.
    2. Build the site:

        ```bash
        uv run mkdocs build --strict
        ```
````

!!! example "Build checklist"

    - [x] Save your Markdown files.
    - [ ] Build the site:

        ```bash
        uv run mkdocs build --strict
        ```

The fence is indented further because it also belongs to the second list item.
Blank lines separate the different blocks.

## Make a section collapsible

Replace `!!!` with `???` for a closed section. Use `???+` to start expanded:

```markdown
??? question "Why use strict mode?"

    Strict mode treats build warnings as failures.

???+ tip "A useful habit"

    Check links in the browser before publishing.
```

??? question "Why use strict mode?"

    Strict mode treats build warnings as failures.

???+ tip "A useful habit"

    Check links in the browser before publishing.

Click the titles to expand or collapse these examples. Keep essential steps in
the main text or an always-visible callout.

## Enable the extensions

This project includes:

```yaml
markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
```

`admonition` handles callouts, `pymdownx.details` adds collapsible sections, and
SuperFences supports nested code fences. Material provides the styling. See the
[Material admonition reference](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)
for more types and options.

## Try it

Write a note containing a prerequisite, a warning describing a consequence, and
a collapsible answer to a common question. Add code inside one callout and
verify the nesting in the preview.

**Next:** [Advanced Features & MkDocs Integration](advanced.md).
