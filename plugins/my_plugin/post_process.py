from __future__ import print_function

import os
import sys
import subprocess
import csscompressor


def post_process_dot(input_path, output_path):
    output_path += '.svg'
    args = ['dot', '-Tsvg', input_path, '-o', output_path]
    try:
        subprocess.check_call(args)
    except Exception:
        print('An error occurred while running', args, file=sys.stderr)
        raise
    return True


def post_process_css(input_path, output_path):
    with open(input_path) as fp:
        css = fp.read()
    with open(output_path, 'w') as fp:
        fp.write(csscompressor.compress(css))
    return True


def post_process(input_path, output_path, url, settings):
    ext = os.path.splitext(input_path)[1]
    if ext == '.dot':
        return post_process_dot(input_path, output_path)
    elif ext == '.css':
        return post_process_css(input_path, output_path)
    else:
        return False
