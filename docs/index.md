# Example MkDocs

Learn to write useful project documentation with Markdown and Material for MkDocs.
The tutorials pair source examples with rendered results so you can see what each
piece of syntax does.

[Start the Markdown tutorials](markdown/index.md)

## Preview this project

Run these commands from the repository root, with [uv](https://docs.astral.sh/uv/)
installed:

```bash
uv sync
uv run mkdocs serve
```

Open the local address printed in your terminal, usually
`http://127.0.0.1:8000`. Edit a file under `docs/`, save it, and the preview reloads.
Stop the server with **Ctrl+C**.

## Build the documentation

```bash
uv run mkdocs build --strict
```

The generated website is written to `site/`. Strict mode fails on warnings,
helping catch missing pages and broken documentation links before publishing.

!!! note "Rendering in the browser"

    Equations use MathJax loaded from a CDN. Material also loads Mermaid when a
    page contains a diagram. Both need JavaScript and access to their external
    scripts; a successful build alone does not confirm browser rendering.
