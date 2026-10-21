# example-mkdocs API

Reference documentation for the modules in `example-mkdocs`, generated from
their source and docstrings.

## Using the plotting module

`calculate_sample_count` chooses enough points for at least 30 samples per cycle.
`WavePlotter` draws the sinusoid on a new or existing Matplotlib axis, while the
module-level `plot_sinusoid` function also displays the figure.

For example, from the repository root:

```bash
uv run python -m example-mkdocs.plotting_example --frequency 2 --duration 5
```

See the [mkdocstrings tutorial](../markdown/mkdocstrings.md) for configuration 
and syntax when generating such APIs.

::: plotting_example
    options:
      heading_level: 2
      show_root_heading: true
      show_root_full_path: false
      filters: ["!^_"]
