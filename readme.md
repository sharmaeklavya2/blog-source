# Blog Source

My blog is generated using Pelican.
Pelican is a static-site generator, which means that
I write blog posts in markdown files and Pelican uses those files to generate a blog website for me.

This repository contains:

* My blog posts in markdown. These are located in the directory `content`.
* Settings for Pelican in `pelicanconf.py`.
* My pelican plugin for customizing the site-generation process, located in `plugins/my_plugin`.


### Generating a site from source

* Install dependencies: `pip install -r requirements.txt`.

* Get a pelican theme (like [MFPelicanTheme](https://github.com/sharmaeklavya2/MFPelicanTheme)).
  Place the theme's directory at `theme` or create a symlink.

* To generate a website for local testing, run `make local`.
  The website will be generated in the directory `output`.
  You also have the option of creating a symlink to a directory at `output`
  before running `make local`.

* To generate a website for deployment, run `make deploy`.
  The website will be generated in the directory `deploy`.
  You also have the option of creating a symlink to a directory at `deploy`
  before running `make deploy`.
