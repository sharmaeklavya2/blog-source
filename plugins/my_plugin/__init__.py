import os
from os.path import join as pjoin
from pelican import signals
from .post_process import post_process

staticfiles = None
seen_file_pairs = set()  # workaround for bug: https://github.com/getpelican/pelican/pull/2593


def inspect_static_generator(static_generator):
    global staticfiles
    staticfiles = static_generator.staticfiles


def post_process_staticfiles(pelican):
    count = 0
    for sc in staticfiles:
        if (sc.source_path, sc.save_as) not in seen_file_pairs:
            count += post_process(input_path=pjoin(pelican.path, sc.source_path),
                output_path=pjoin(pelican.output_path, sc.save_as),
                url=sc.url, settings=pelican.settings)
            seen_file_pairs.add((sc.source_path, sc.save_as))
    print('post-processed {}/{} static files'.format(count, len(seen_file_pairs)))


def post_process_theme_staticfiles(pelican):
    theme_path = pjoin(pelican.output_path, 'theme')
    count = 0
    fnames = os.listdir(theme_path)
    for fname in fnames:
        fpath = pjoin(theme_path, fname)
        count += post_process(input_path=fpath, output_path=fpath,
                url=None, settings=pelican.settings)
    print('post-processed {}/{} theme static files'.format(count, len(fnames)))


def is_external_url(url):
    return url.startswith('http:') or url.startswith('https:')


def remove_external_articles(article_generator, writer):
    for article in article_generator.articles:
        if is_external_url(article.metadata.get('url', '')):
            ofpath = pjoin(article_generator.output_path, article.save_as)
            try:
                os.remove(ofpath)
            except FileNotFoundError:
                pass


def register():
    signals.static_generator_finalized.connect(inspect_static_generator)
    signals.finalized.connect(post_process_staticfiles)
    signals.finalized.connect(post_process_theme_staticfiles)
    signals.article_writer_finalized.connect(remove_external_articles)
