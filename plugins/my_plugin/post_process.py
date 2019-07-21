import os
import subprocess


def post_process_dot(input_path, output_path):
    output_path += '.svg'
    args = ['dot', '-Tsvg', input_path, '-o', output_path]
    print('post_process_dot: running', args)
    subprocess.check_call(args)


def post_process(input_path, output_path, url, settings):
    ext = os.path.splitext(input_path)[1]
    if ext == '.dot':
        post_process_dot(input_path, output_path)
