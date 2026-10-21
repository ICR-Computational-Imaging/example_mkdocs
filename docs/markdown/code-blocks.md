# 6. Code Blocks & Syntax Highlighting

Code examples preserve whitespace and tell readers which language they use.
This lesson covers inline code and fenced, copyable examples.

## Choose inline code or a block

Use single backticks for commands or identifiers inside a sentence:

```markdown
Run `uv run mkdocs serve` from the repository root.
```

Run `uv run mkdocs serve` from the repository root.

For multiple lines, surround the code with triple backticks on separate lines.
Add a language identifier immediately after the opening fence. To show triple
backticks literally in a tutorial, surround the example with **four** backticks,
as the source of this page does.

## Highlight Python

Write:

````markdown
```python
def greet(name: str) -> str:
    return f"Hello, {name}!"


print(greet("MkDocs"))
```
````

Rendered result:

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"


print(greet("MkDocs"))
```

Whitespace is preserved, including Python indentation. Markdown markers inside
the fence are displayed literally.

## Highlight Bash and YAML

Use `bash` for shell commands. Omit prompts such as `$` so readers can copy
commands directly:

````markdown
```bash
uv run mkdocs serve
```
````

```bash
uv run mkdocs serve
```

Use `yaml` for configuration. This is a minimal example for a separate site;
the full project configuration also enables the tutorial extensions:

````markdown
```yaml
site_name: My documentation
theme:
  name: material
```
````

```yaml
site_name: My documentation
theme:
  name: material
```

Choose `text` for output that needs no language-specific highlighting:

```text
Hello, MkDocs!
```

## Add a title and line numbers

Material supports extra fence options through its highlighting extensions:

````markdown
```python title="greeting.py" linenums="1" hl_lines="2"
def greet(name: str) -> str:
    return f"Hello, {name}!"
```
````

```python title="greeting.py" linenums="1" hl_lines="2"
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

`title` names the example, `linenums` sets its starting line number, and
`hl_lines` emphasises selected lines.

## Enable highlighting and copying

This project's configuration includes:

```yaml
theme:
  name: material
  features:
    - content.code.copy

markdown_extensions:
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.superfences
```

Material adds the copy button. Pygments handles language highlighting at build
time, and SuperFences supports fenced blocks nested inside lists and callouts.
The actual project also configures a Mermaid custom fence on the SuperFences
entry; retain those options when editing it.

See the [Material code-block reference](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/)
for further options.

## Try it

Write a Python example, a Bash command, and a YAML configuration fragment. Add a
filename title to the Python block. Use its copy button in the preview and check
that the copied text contains the code without the Markdown fences.

**Next:** [Tables](tables.md).
