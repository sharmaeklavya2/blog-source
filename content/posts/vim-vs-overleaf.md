title: Vim vs Overleaf
slug: vim-vs-overleaf
tags: web-dev
ExtraCSS: css/solarized.css
date: 2026-01-17
summary: Why editing LaTeX documents locally is better than Overleaf.


In this article, I compare these two approaches to editing LaTeX documents on Overleaf:

1.  Edit directly using Overleaf's editor.
2.  My setup: fetch from Overleaf using git, edit locally (using vim, pdflatex, and macOS Preview),
    and push to Overleaf using git.

[TOC]


## Details of My Setup

I edit latex code in vim and sync it to Overleaf using Git.

## Advantages of Local Editing over Overleaf

1.  Offline use:
    Very useful in flights or areas with spotty connectivity.
    Danger of losing changes with Overleaf?
2.  Git:
    For checking diffs, branching, selectively committing/discarding changes.
3.  Fully customizable editor.
4.  With local PDF viewer, I can go back after clicking a hyperref.
5.  Overleaf's custom PDF viewer doesn't have bookmarks sidebar.
    I can use browser's PDF viewer instead of Overleaf's custom viewer
    to get back bookmarks, but then I lose dark mode and synctex.

## Advantages of Overleaf over Local Editing

1.  Simultaneous editing
2.  SyncTex: can jump from position in PDF to position in code and vice versa.

## Features available in Both Setups

1.  Smart Autocomplete:
    Using the TexLab plugin in Vim.
2.  Dark mode PDFs:
    As of Feb 2026, Overleaf does this using the CSS filter
    `invert(95%) hue-rotate(180deg) brightness(90%) contrast(90%);`.
    When building PDFs locally, I use
    [github:sharmaeklavya2/tex-colorscheme](https://github.com/sharmaeklavya2/tex-colorscheme/).
    Overleaf's solution is much cleaner here.
