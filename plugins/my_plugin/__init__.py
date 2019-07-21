from os.path import join as pjoin
from pelican import signals
from .post_process import post_process

staticfiles = None
seen_file_pairs = set()  # workaround for bug: https://github.com/getpelican/pelican/pull/2593


def inspect_static_generator(static_generator):
    global staticfiles
    staticfiles = static_generator.staticfiles


def post_process_hook(pelican):
    for sc in staticfiles:
        if (sc.source_path, sc.save_as) not in seen_file_pairs:
            post_process(input_path=pjoin(pelican.path, sc.source_path),
                output_path=pjoin(pelican.output_path, sc.save_as),
                url=sc.url, settings=pelican.settings)
            seen_file_pairs.add((sc.source_path, sc.save_as))
    print('post-processed {} static files'.format(len(seen_file_pairs)))


def register():
    signals.static_generator_finalized.connect(inspect_static_generator)
    signals.finalized.connect(post_process_hook)
