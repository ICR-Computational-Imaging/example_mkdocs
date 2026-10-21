# 3. Text Formatting

Formatting helps readers identify actions, important terms, and literal values.
This lesson covers emphasis, strikethrough, inline code, and separators.

## Add emphasis

```markdown
Use **bold** for an important action.
Use *italic* for gentle emphasis or a newly introduced term.
Use ***bold italic*** sparingly.
```

Use **bold** for an important action.
Use *italic* for gentle emphasis or a newly introduced term.
Use ***bold italic*** sparingly.

Keep markers next to the text: `**important**` works, whereas `** important **`
does not create the intended emphasis. Underscores can also mark emphasis;
asterisks offer a consistent style for prose.

## Show strikethrough

```markdown
The output is ~~results.csv~~ **summary.csv**.
```

The output is ~~results.csv~~ **summary.csv**.

Strikethrough needs an extension in this renderer. This project enables it with:

```yaml
markdown_extensions:
  - pymdownx.tilde
```

## Mark literal text with inline code

Surround a command, filename, option, or variable with backticks:

```markdown
Run `mkdocs serve` and edit `docs/index.md`.
The option is named `--strict`.
```

Run `mkdocs serve` and edit `docs/index.md`.
The option is named `--strict`.

Formatting is not interpreted inside code spans: `**bold**` shows its asterisks
literally. To show a backtick itself, use a longer delimiter:

```markdown
Use `` `value` `` to show a value surrounded by backticks.
```

Use `` `value` `` to show a value surrounded by backticks.

## Add a horizontal rule

Put three hyphens on their own line, with blank lines on both sides:

```markdown
End of the first topic.

---

Beginning of the next topic.
```

End of the first topic.

---

Beginning of the next topic.

Without the preceding blank line, hyphens below text can be interpreted as an
alternative heading syntax. Use headings for the outline and rules for occasional
visual breaks.

## Escape formatting characters

Place a backslash before a Markdown marker to show it literally:

```markdown
Write \*sample\* to show the asterisks.
```

Write \*sample\* to show the asterisks.

## Try it

Write a release note with a bold action, an italic term, a filename in inline
code, a crossed-out old filename, and a horizontal rule. Preview the result.

**Next:** [Lists & Task Lists](lists.md).
