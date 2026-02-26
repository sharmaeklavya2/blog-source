title: Vim vs Overleaf
slug: vim-vs-overleaf
tags: latex
date: 2026-02-25
summary: Why editing LaTeX documents locally is better than Overleaf.


In this article, I compare these two approaches to editing LaTeX documents on Overleaf:

1.  Edit directly using Overleaf's editor.
2.  My setup: fetch from Overleaf using git, edit locally (using vim, `pdflatex`, and macOS Preview),
    and push to Overleaf using git.

[TOC]


## Advantages of Local Editing over Overleaf

1.  **Offline use**:
    Local editing is very useful in flights or areas with spotty connectivity.
    Sometimes I have lost changes with Overleaf.
2.  I can **use git** to check diffs, create branches, and selectively commit/discard changes.
3.  With a local PDF viewer, I can **go back** after clicking a hyperref.
4.  Overleaf's custom PDF viewer doesn't have the **bookmarks sidebar**.
    I can use the browser's PDF viewer instead of Overleaf's custom viewer
    to get back bookmarks, but then I lose dark mode and synctex.
5.  **Spellcheck**: Vim can iterate over typos. Vim can have per-project `spellfile`s.
6.  In vim I can `set scrolloff=8`. Then vim starts scrolling the screen
    a few lines before the cursor reaches the end of screen.

## Advantages of Overleaf over Local Editing

1.  Multiple people can **simultaneously edit** the document.
2.  **SyncTex**: I can jump from position in PDF to position in code and vice versa.

## Features Available in Both Setups

1.  Smart Autocomplete:
    In vim, this can be achieved using the TexLab plugin.
2.  Dark mode PDFs:
    As of Feb 2026, Overleaf does this using the CSS filter
    `invert(95%) hue-rotate(180deg) brightness(90%) contrast(90%);`.
    When building PDFs locally, I use
    [github:sharmaeklavya2/tex-colorscheme](https://github.com/sharmaeklavya2/tex-colorscheme/).
    Overleaf's solution is much cleaner here.
