# 5. Links & Images

Links connect readers to information, and images illustrate concepts. This
lesson uses real pages and the logo included in this repository.

## Link to a website

Put descriptive link text in square brackets and the URL in parentheses:

```markdown
Read the [MkDocs documentation](https://www.mkdocs.org/).
```

Read the [MkDocs documentation](https://www.mkdocs.org/).

Prefer descriptive labels over “click here”, so destinations are clear when
scanning a page or using assistive technology.

## Link between documentation pages

Use source Markdown paths relative to the file you are editing:

```markdown
[Text formatting](text-formatting.md)
[Project home](../index.md)
[Heading syntax](headings.md#write-headings)
```

- [Text formatting](text-formatting.md) is in the same folder as this page.
- [Project home](../index.md) is one folder above this page.
- [Heading syntax](headings.md#write-headings) opens a section on another page.

MkDocs rewrites recognised `.md` page links into generated website URLs,
including directory-style URLs when `use_directory_urls: true` is set.

Paths in `nav` are different: they are relative to `docs_dir`, which is `docs/`
here. A link from this page to `headings.md` corresponds to
`markdown/headings.md` in the navigation configuration.

## Embed an image

An image uses link syntax with an exclamation mark. The text in square brackets
is alternative text describing the image:

```markdown
![Example MkDocs logo: an open book forming an M](../assets/logo.svg)
```

![Example MkDocs logo: an open book forming an M](../assets/logo.svg)

The path starts at `docs/markdown/`, moves up to `docs/`, and enters `assets/`.
SVG works well for logos because it stays sharp at different sizes.

## Set an image width

With `attr_list` enabled, put attributes after the image:

```markdown
![Example MkDocs open-book logo](../assets/logo.svg){ width="64" }
```

![Example MkDocs open-book logo](../assets/logo.svg){ width="64" }

```yaml
markdown_extensions:
  - attr_list
```

## Link an image to a page

Wrap the entire image expression in a normal link:

```markdown
[![Open the tutorial overview](../assets/logo.svg)](index.md)
```

[![Open the tutorial overview](../assets/logo.svg)](index.md)

## Check your paths

Match file names and capitalisation exactly, including on case-sensitive hosting
systems. Avoid leading `/` for project-local links: absolute site paths can break
when hosting under a repository name. Build with `uv run mkdocs build --strict`
to help catch missing documentation targets.

## Try it

Add a link to another lesson, a link to a heading in that lesson, and the logo at
a width of 80 pixels. Open the links in the preview and check the image's
alternative text in the source.

**Next:** [Code Blocks & Syntax Highlighting](code-blocks.md).
