title: Making a keyboard-navigable collapsible without JavaScript
slug: css-collapsible
tags: Web dev, Tutorial
ExtraCSS: css/collapsible.css, css/pygments-manni.css
date: 2018-11-01
summary: A 'collapsible' is content whose visibility can be toggled by clicking something. However, users without a mouse should also be able to open the collapsed content. This article explains how to make a keyboard-navigable collapsible without using JavaScript.


A 'collapsible' is content whose visibility can be toggled. Here is an example:

<div class="collapsible" style="clear: both">
    <label for="checkbox0" class="collapsor-lbl"> Click me </label>
    <div class="focus-capturer" tabindex="0">
        <input id="checkbox0" class="collapsor" type="checkbox" />
        <div class="collapsible-content">
            <p>This is the body of the collapsible. Its visibility can be toggled using the 'click me' button.</p>
            <p>Here we will learn how to make such a collapsible without using JavaScript.</p>
        </div>
    </div>
</div>

In this article, we'll look at how to make one.

[TOC]


## Skeleton

Let's first create the basic structure without collapsibility.

HTML:

    :::html
    <div class="collapsible">
        <div class="collapsor-lbl"> Click me </div>
        <div class="collapsible-content">
            This is the body of the collapsible.
        </div>
    </div>

CSS (for beautification):

    :::css
    .collapsible {
        max-width: 40em;
        border: 1px solid black;
        border-radius: 0.5rem;
    }
    .collapsor-lbl:hover {
        background-color: rgba(0, 0, 0, 0.1);
    }
    .collapsor-lbl {
        text-align: center;
        padding: 0.5rem 1rem;
    }
    .collapsible-content {
        padding: 0.5rem;
        border-top: 1px solid black;
    }

This is what the output looks like:

<div class="collapsible">
    <div class="collapsor-lbl"> Click me </div>
    <div class="collapsible-content" style="display: block">
        This is the body of the collapsible.
    </div>
</div>

## Collapsibility

To add collapsibility, we're going to use a checkbox.
I read about it on the blog post
'[Implementing A Pure CSS Collapsible](https://alligator.io/css/collapsible/)' by alligator.io.

* A checkbox maintains state about whether it's checked or not.
  We can use that to maintain state about whether our collapsible has been clicked or not.
* We can use the CSS style `display:none` to make the checkbox disappear, but still retain its functionality.
* We can use the CSS pseudo-selector `:checked` to select a checked checkbox.
* We will make sure that `.collapsible-content` is a sibling of the checkbox.
  Then we can use the CSS sibling combinator '`~`' to select it.
  When used together with `:checked` on checkbox, we can select `.collapsible-content` only when the checkbox is checked.

Change the HTML to this:

    :::html
    <div class="collapsible">
        <input id="checkbox1" class="collapsor" type="checkbox" />
        <label for="checkbox1" class="collapsor-lbl"> Click me </label>
        <div class="collapsible-content">
            This is the body of the collapsible.
        </div>
    </div>

Add this CSS:

    :::css
    .collapsor-lbl {
        display: block;
    }
    .collapsor, .collapsible-content {
        display: none;
    }
    .collapsor:checked ~ .collapsible-content {
        display: block;
    }

Output:

<div class="collapsible">
    <input id="checkbox1" class="collapsor" type="checkbox" />
    <label for="checkbox1" class="collapsor-lbl"> Click me </label>
    <div class="collapsible-content">
        This is the body of the collapsible.
    </div>
</div>

## Accessibility

> Web accessibility is the inclusive practice of ensuring there are no barriers that
> prevent interaction with, or access to websites, by people with disabilities.
> <footer>[Wikipedia article on Web Accessibility](https://en.wikipedia.org/wiki/Web_accessibility)</footer>

I once had a mouse that sometimes stopped functioning, so I can feel a bit of the pain of users who cannot use a mouse.
Also, some people *like* using the keyboard for navigation and it would be bad to force them to use a mouse.

I don't know much about web accessibility standards and what it takes for my websites to be fully accessible,
but the least I can do is make my pages keyboard-navigable.

The [blog post by alligator.io](https://alligator.io/css/collapsible/#a-note-on-accessibility)
says how to make a collapsible using only CSS, but to make it accessible they had to use JavaScript.
I, however, have a way of doing it without JavaScript.

When navigating a web page using the tab key, certain HTML elements have the potential of receiving focus.
This generally includes links (`<a>` tags) and form elements (`<input>` tags).
When an element receives focus, it gets the `:focus` CSS pseudo-class.
Also, that element and all its descendants get the `:focus-within` class.

We will therefore wrap `.collapsible-content` within a `<div>`.
We will make that `<div>` capable of receiving focus via tab by setting the attribute `tabindex` to `"0"`.
Then whenever that div has the `:focus-within` pseudo-class set,
we will set `display: block` on `.collapsible-content`.

Change the HTML to this:

    :::html
    <div class="collapsible">
        <label for="checkbox2" class="collapsor-lbl"> Click me </label>
        <div class="focus-capturer" tabindex="0">
            <input id="checkbox2" class="collapsor" type="checkbox" />
            <div class="collapsible-content">
                <p>This is the body of the collapsible.<p>
                <ul>
                    <li><a href="">link1</a></li>
                    <li><a href="">link2</a></li>
                    <li><a href="">link3</a></li>
                </ul>
            </div>
        </div>
    </div>

Add this CSS:

    :::css
    .focus-capturer:focus-within .collapsible-content {
        display: block;
    }

Output:

<div class="collapsible">
    <label for="checkbox2" class="collapsor-lbl"> Click me </label>
    <div class="focus-capturer" tabindex="0">
        <input id="checkbox2" class="collapsor" type="checkbox" />
        <div class="collapsible-content">
            <p>This is the body of the collapsible.</p>
            <ul>
                <li><a href="">link1</a></li>
                <li><a href="">link2</a></li>
                <li><a href="">link3</a></li>
            </ul>
        </div>
    </div>
</div>

Try using the tab key to navigate all the 3 links in the collapsible.
When the focus moves out of the collapsible, it closes (unless you had clicked on it to open it).

Navigation using Shift+Tab is a bit wonky though.

## Use

When my blog's website is viewed on a screen of size less than 800 pixels, the navigation bar moves to the top.
It becomes collapsible and users have to click the '&equiv;' button to open it.
I have used the above technique to implement this collapsible navigation bar.

Feel free to [reach out](https://github.com/sharmaeklavya2/blog/issues/new)
for comments, criticism or suggestions.
