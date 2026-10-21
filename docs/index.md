# Example MkDocs

![Site logo](assets/logo.svg)

Learn to write useful project documentation with [MkDocs](https://www.mkdocs.org/)
and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/getting-started/).
The [tutorials](markdown/index.md) pair source examples with rendered results so you can see what specific syntax does.

!!! note "Future development"
    The team behind Material for MkDocs is migrating their work to a new platform
    [`zeniscal`](https://zensical.org/docs/compatibility/mkdocs/migration/).
    We need to watch this space and adapt accordingly.

## Preview and edit this project

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

The generated website `html` files are written to `site/`. Strict mode fails on warnings,
helping catch missing pages and broken documentation links before publishing.
