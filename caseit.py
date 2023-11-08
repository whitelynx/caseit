#!/usr/bin/env python

import argparse
import re
import sys

import stringcase


collapse_whitespace_re = re.compile(r'\s+')


parser = argparse.ArgumentParser(description='Convert the case of text from stdin.')
for flags in (
    ('a', 'alphanumcase'),
    ('b', 'backslashcase'),
    ('c', 'camelcase'),
    ('C', 'capitalcase'),
    ('n', 'constcase'),
    ('d', 'dotcase'),
    ('l', 'lowercase'),
    ('P', 'pascalcase'),
    ('p', 'pathcase'),
    ('S', 'sentencecase'),
    ('s', 'snakecase'),
    ('k', 'kebabcase', 'spinalcase'),
    ('T', 'titlecase'),
    ('t', 'trimcase'),
    ('u', 'uppercase'),
):
    func_name = flags[-1]
    func = getattr(stringcase, func_name)
    description = collapse_whitespace_re.sub(' ', func.__doc__.split('\n\n', 1)[0])

    parser.add_argument(
        *[('-' if len(flag) == 1 else '--') + flag for flag in flags],
        dest='transform',
        action='store_const',
        const=func,
        help=description
    )

args = parser.parse_args()

if args.transform is None:
    parser.print_help()
    sys.exit(1)

while True:
    try:
        input_text = input()

        print(args.transform(input_text))
    except EOFError:
        break
