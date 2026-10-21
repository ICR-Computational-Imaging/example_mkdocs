# API Documentation with mkdocstrings

[mkdocstrings](https://mkdocstrings.github.io/python/usage/) is a MkDocs plugin
that generates API reference sections from Python source and docstrings. It keeps
function signatures, parameter descriptions, return values, and class members
connected to the code they describe. Write tutorials and usage guidance yourself;
use generated reference material for the details of individual objects.

## Enable the Python handler

This project's `docs` dependency group already includes `mkdocstrings[python]`.
Install that group and start the preview from the repository root:

```bash
uv sync --group docs
uv run --group docs mkdocs serve
```

For another uv project, add the dependency with
`uv add --group docs 'mkdocstrings[python]'`.

The following configuration is enabled in this project's `mkdocs.yaml`:

```yaml
--8<-- "mkdocs.yaml:mkdocstrings"
```

`paths` tells the handler where to find modules; relative paths start at the
MkDocs configuration file. Here, it can find `plotting_example.py` directly in
`src/example-mkdocs/`. Additional locations can be added to this list.

## Use the standard directive syntax

Place `:::` followed by an object's dotted identifier in a Markdown page:

```markdown
::: plotting_example.calculate_sample_count
```

The directive can target a module, class, function, or method. These are examples
of valid targets in this project:

```text
plotting_example
plotting_example.WavePlotter
plotting_example.WavePlotter.plot_sinusoid
plotting_example.calculate_sample_count
```

Put a directive outside a code fence to generate documentation. The fenced
examples on this tutorial page deliberately display the syntax as text.

Indent optional YAML settings four spaces below the directive:

```markdown
::: plotting_example.calculate_sample_count
    options:
      heading_level: 2
      show_root_heading: true
      show_source: false
```

Local `options` override the handler defaults for that directive.
`show_root_heading` adds a heading for the target object itself, and
`heading_level` controls where it fits in the page outline.

## Write structured docstrings

This project uses Google-style sections such as `Args:`, `Returns:`, and
`Raises:`. Type annotations supply parameter types. For example, a small function
could be documented as follows:

```python
def double(value: float) -> float:
    """Return twice the input value.

    Args:
        value: The number to double.

    Returns:
        Twice the input value.
    """
    return 2 * value
```

The handler turns these sections into formatted API information. This snippet
illustrates docstring style; `double` is not a module in the repository.

## Example: document the plotting module

The [example-mkdocs API reference](../api/example-mkdocs.md) contains this live
directive:

```markdown
::: plotting_example
    options:
      heading_level: 2
      show_root_heading: true
      show_root_full_path: false
      filters: ["!^_"]
```

It collects the module's public members, including `calculate_sample_count`,
`WavePlotter`, and the convenience function `plot_sinusoid`. The filter excludes
names beginning with `_`, such as the internal `_parse_args` helper. Public
methods such as `WavePlotter.plot_sinusoid` appear under their class.

For example, the sampling function returns **301** for 1 Hz over 10 seconds:

```python
calculate_sample_count(frequency=1.0, duration=10.0)
```

mkdocstrings renders the API description; it does not run this example or verify
the calculation. That still needs normal code validation.

## Group API pages by purpose

MkDocs supports nested sections in `nav`; it does not require a flat tree.
Use one page for a small group of related modules and give each module its own
directive. Split large modules onto separate pages so readers do not have to
scroll through unrelated objects. A useful pattern for a larger package is:

```yaml
nav:
  - API reference:
      - Data:
          - Loading: api/data/loading.md
          - Processing: api/data/processing.md
      - Plotting: api/plotting.md
```

This is an illustrative layout for a larger project, not additional pages in
this repository. Folders can guide the grouping without dictating every menu
level. The [MkDocs navigation guide](https://www.mkdocs.org/user-guide/writing-your-docs/#configure-pages-and-navigation)
explains nested sections.

This project currently has one source module, so one API page is enough. If a
second related module is added, it can have another directive on that page;
adding a source file alone does not automatically add a new API directive.
Document each object in one canonical location to avoid duplicate reference
targets, then link to it from tutorials.

## Try it

Open the API reference and find the parameters, return description, and exceptions
for `calculate_sample_count`. Compare them with its source docstring. Then build
the site to check that all directives resolve:

```bash
uv run --group docs mkdocs build --strict
```
