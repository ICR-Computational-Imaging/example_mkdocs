# 8. Mathematical Equations

Write mathematical notation with LaTeX syntax inside dollar delimiters. This
project uses Arithmatex to recognise equations and MathJax to render them in the
browser.

## Write an inline equation

Single dollar signs keep an equation in a sentence:

```markdown
Mass and energy are related by $E=mc^2$.
```

Mass and energy are related by $E=mc^2$.

Keep delimiters next to the expression. For literal currency, escape the dollar
sign, as in `\$20`, to avoid accidental maths parsing.

## Write a display equation

Use double dollar signs on separate lines. Leave blank lines around the block:

```latex
$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i
$$
```

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i
$$

Here, $x_i$ is the $i$th observation, $n$ is the number of observations, and
$\bar{x}$ is their arithmetic mean. Define symbols in the surrounding prose.

The `latex` code block displays source for teaching. To render the equation,
paste its contents into Markdown **without** a code fence.

## Learn common LaTeX commands

| Meaning | Source | Result |
| :--- | :--- | :--- |
| Superscript | `x^{10}` | $x^{10}$ |
| Subscript | `x_{ij}` | $x_{ij}$ |
| Fraction | `\frac{a}{b}` | $\frac{a}{b}$ |
| Square root | `\sqrt{x}` | $\sqrt{x}$ |
| Greek letters | `\alpha + \beta` | $\alpha + \beta$ |
| Summation | `\sum_{i=1}^{n} x_i` | $\sum_{i=1}^{n} x_i$ |
| Text in maths | `\text{accuracy}` | $\text{accuracy}$ |

Braces group multiple characters in a superscript or subscript. For example,
`x^10` raises only the `1`; use `x^{10}` for the entire exponent.

## Configure MathJax

These settings are already in this repository's `mkdocs.yaml`:

```yaml
markdown_extensions:
  - pymdownx.arithmatex:
      generic: true

extra_javascript:
  - assets/javascripts/mathjax.js
  - https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-mml-chtml.js
```

The local file `docs/assets/javascripts/mathjax.js` configures the delimiters
produced by Arithmatex and must load before MathJax:

```javascript
window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};
```

Arithmatex converts dollar-delimited expressions to wrappers that MathJax
typesets after the page loads. This project uses ordinary full-page navigation.
If you later enable `navigation.instant`, also add the re-typesetting lifecycle
integration in the [Material maths reference](https://squidfunk.github.io/mkdocs-material/reference/math/).

## Understand the KaTeX alternative

KaTeX is another browser renderer for LaTeX maths. To switch, retain Arithmatex
with `generic: true`, replace the MathJax scripts with KaTeX's library and
auto-render script, load its CSS, and configure auto-render to recognise
`\(...\)` and `\[...\]`. Its supported commands differ, so check your equations
after switching. Choose one renderer rather than loading both. The
[official KaTeX integration example](https://squidfunk.github.io/mkdocs-material/reference/math/#katex)
shows the assets and initialisation.

## Troubleshoot rendering

If raw delimiters remain visible, check that the equation is outside a code
fence, Arithmatex is enabled, and MathJax loads successfully. Rendering needs
JavaScript and access to the CDN; building HTML does not typeset the equations.

## Try it

Write the inline expression `$y=mx+b$`, followed by a display equation containing
`\sigma = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(x_i-\bar{x})^2}`. Define the symbols
and check that the preview shows a root, fraction, sum, and subscripts.

**Next:** [Admonitions & Callouts](admonitions.md).
