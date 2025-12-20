title: Dark Mode for Everything
slug: dark-mode
date: 2025-12-20
ExtraCSS: css/solarized.css
summary: Tips and tricks on getting dark mode everywhere


In the last decade, dark mode has become a staple feature of most operating systems,
and many apps and websites now adapt to it. Unfortunately, it's not ubiquitous enough.
If it's really dark around me, any website or app that's in light mode becomes unbearably bright,
and so, I set out to figure out how to enable dark mode for <strong>everything</strong>.
This article documents my findings.

Additionally, if I'm sitting out in the sun, dark mode can be a bit too dark, so I want light mode then.
This means I want to avoid hard-coding everything to always be in dark mode.

[TOC]

## The Basics

I'm assuming you know how to set/unset dark mode in your OS.
In macOS Tahoe, even after switching to dark mode, app icons are in light mode by default.
You can change that in Systems Settings > Appearance > Icon & widget style.

I think you'd want to use a dark wallpaper, or if your OS supports it,
different wallpapers depending on the system theme.
In macOS, custom auto-switching wallpapers can be created using the [Equinox app](https://equinoxmac.com/).

## Web

Many websites automatically switch to dark mode, but not all.
On desktop, I use the [Dark Reader](https://darkreader.org/) browser extension.
It changes websites' colors to forcefully convert them to dark mode if needed.
I haven't tried Dark Reader on my phone yet.

### Writing your own web pages

I have created many websites from scratch, and I have enabled dark mode for them all.
Doing this is usually quite simple. First, add the following in your HTML's `<head>`:

    :::html
    <meta name="color-scheme" content="light dark" />

This is to tell the browser that we allow both light and dark color schemes on our web page.
Then things like scrollbars and checkboxes will be shown in the right color scheme.
If you haven't set the background and text color in CSS yourself,
the browser will pick values for them too based on the color scheme.

If you write your own HTML, you're probably using your own CSS too.
Whenever you set a color for something (text, background, or borders) in CSS,
you'd need a way to specify colors for both the dark and light themes.
This can be easily done using the
[`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme) media feature and the [`var`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var) CSS function.
In your CSS, start with a color scheme section, like this:

    :::css
    body {
        --text-color: #202020;
        --bg-color: white;
        --link-color: #1a0dab;
    }
    @media (prefers-color-scheme: dark) {
        body {
            --text-color: #c8c8c8;
            --bg-color: #1b1e20;
            --link-color: #8ab4f8;
        }
    }

Then use the colors like this:

    :::css
    body {
        color: var(--text-color);
        background-color: var(--bg-color);
    }
    a {
        color: var(--link-color);
    }

Images can be more difficult to deal with.
If they are photographs, you can reduce their brightness using this CSS:
`filter: brightness(.8) contrast(1.2);`.
If they are icons or diagrams, you can invert colors like this:
`filter: brightness(.85) invert(1) brightness(.75) hue-rotate(180deg);`

### Nginx autoindex

If you're using [nginx](https://nginx.org/) with `autoindex`,
you may want the resulting index pages to be in dark mode too.
You can find the instructions
[here](https://sharmaeklavya2.github.io/blog/customize-macos.html#enable-nginx-autoindex).
These instructions are written for macOS;
you'd have to translate them for your OS.

## PDFs

PDF readers can often easily switch their UI (toolbars, etc.) to dark mode,
but switching the PDFs themselves to dark mode is, of course, not easy.

Preview, the default PDF app in macOS, doesn't support changing the colors of the PDF,
but Adobe's Acrobat Reader does.
In Acrobat Reader, go to Preferences > Accessibility, and check 'Replace Document Colors'.
Select 'Custom Colors'. Then specify the colors for 'Page Background' and 'Document Text'
I recommend `#151718` and `#bdbdbc`, respectively.
Now you can switch between light and dark modes by simply
toggling the 'Replace Document Colors' checkbox.

The above would have been a very satisfactory solution if Acrobat Reader was an otherwise good PDF reader.
Moreover, colored text is still not handled well in this solution.
I often read LaTeX-generated PDFs, where the colors of citations and links are specified using
`linkcolor`, `citecolor`, `urlcolor` in `\hypersetup`.
Most papers use dark or fully-saturated colors here, which are fine for light mode but not for dark mode.

For PDFs that I write in LaTeX, I just generate them in dark mode.
See [`colorscheme.tex`](https://github.com/sharmaeklavya2/tex-colorscheme/)
for TeX macros I wrote for this and how to use them.

ArXiv fortunately lets us download the TeX source of papers.
I can build those papers in dark mode by adding `\input{colorscheme.tex}`
and changing the colors used in `\hypersetup`.
I wrote a Python script to automate this:
[`from-arxiv.py`](https://github.com/sharmaeklavya2/from-arxiv).

## Terminal

I use [iTerm2](https://iterm2.com/), which automatically switches the terminal colors based on the system theme.
My `.vimrc` tries to detect the system theme and set vim's `background` accordingly.
See my [dotfiles](https://github.com/sharmaeklavya2) for more info.
