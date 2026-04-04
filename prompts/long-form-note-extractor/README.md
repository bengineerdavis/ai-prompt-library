# Long-form Note Extractor

## Overview

The **Long-form Note Extractor** is a direct-use prompt for turning long-form content into reusable notes. It works for both technical and non-technical topics and is optimized for personal knowledge bases, research and study notes, documentation support, and general “future me” reference.

This is **not** a factory. It is a regular prompt intended for direct use with pasted content or extracted transcripts.

## Use cases

- Extract notes from podcast, talk, lecture, or video transcripts.
- Summarize and structure long blog posts, essays, and articles.
- Capture key concepts, arguments, evidence, and references from research material.
- Turn documentation or technical articles into reusable notes.
- Build durable personal notes for later review.

## Defaults

- `OUTPUT_FORMAT`: `zim`
- `PRIMARY_GOAL`: `high-quality notes and summary`
- `MAX_LENGTH_NOTES`: `no hard limit`
- `AUDIENCE`: `future me`
- `STRICTNESS`: `balanced`

## Parameters

The prompt auto-detects or accepts these parameters:

- `CONTENT_SOURCE`: `podcast | video | talk | blog | docs | other`
- `TOPIC_OR_TITLE`: explicit title if present, otherwise inferred
- `OUTPUT_FORMAT`: `zim | markdown | txt`
- `PRIMARY_GOAL`
- `MAX_LENGTH_NOTES`
- `AUDIENCE`
- `STRICTNESS`: `literal | balanced | interpretive`

## Output structure

The prompt produces, in order:

1. Parameters used
2. Capability note
3. Metadata header in the selected format
4. Outline summary
5. Detailed notes
6. Fact capture
7. Sources mentioned
8. Actions & questions
9. Full cleaned transcript, when applicable

## Capabilities

The prompt is designed to be capability-aware.

It should:

- detect whether it can process the given input format directly
- detect whether it can transcribe audio/video or only work from text
- note whether current-date lookup is verified or unavailable
- explain specific reasons when a format cannot be processed
- avoid inventing model, service, capability, or source-link details

## Output formats

### ZimWiki

Zim uses its own wiki syntax, including `=`-based headings, `*` bullets, checkboxes, and wiki-style formatting.[web:4][web:6]

Use `OUTPUT_FORMAT: zim` when your destination is Zim desktop wiki or another Zim-compatible notebook.

### Markdown

Markdown output should use mainstream Markdown with GitHub-Flavored Markdown-compatible conventions such as `#` headings, standard lists, and fenced code blocks.[web:15][web:19]

Use `OUTPUT_FORMAT: markdown` for README-style notes, documentation, or Markdown-based note systems.

### Plain text

Use `OUTPUT_FORMAT: txt` when markup is undesirable or when you want a minimal plain-text archive.

## Source tracking

The prompt includes a `Sources mentioned` section that attempts to capture references explicitly named in the source material.

For each source, it should:

- identify the source as precisely as possible
- include a link when one is reliably available
- add a very brief contextual description
- avoid inventing links when uncertain

## File layout

```text
[prompt-library]/
  prompts/
    long-form-note-extractor/
      README.md
      prompt.md
```

## Version

- Version: `1.0`
- Status: `production-ready direct-use prompt`
