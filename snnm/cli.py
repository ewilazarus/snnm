import argparse
import sys

from .scrape import scrape
from .style import adorn


def parse(args):
    parser = argparse.ArgumentParser(
        prog='snnm',
        description='Get a list of synonyms from http://www.thesaurus.com'
    )
    parser.add_argument(
        'term',
        metavar='TERM',
        help='a string TERM representing the lookup term'
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-m',
        '--mixed-case',
        action='store_const',
        help='display the synonyms in mixedCaseStyle',
        dest='style',
        const='mixed'
    )
    group.add_argument(
        '-c',
        '--camel-case',
        action='store_const',
        help='display the synonyms in CamelCaseStyle',
        dest='style',
        const='camel'
    )
    group.add_argument(
        '-u',
        '--underscore',
        action='store_const',
        help='display the synonyms in lower case with underscore_style',
        dest='style',
        const='underscore'
    )
    group.add_argument(
        '-o',
        '--constant',
        action='store_const',
        help='display the synonyms in CONSTANT_STYLE',
        dest='style',
        const='constant'
    )
    return parser.parse_args(args)


def main():
    args = parse(sys.argv[1:])
    synonyms = scrape(args.term)
    synonyms = adorn(synonyms, args.style)
    for s in synonyms:
        print(s)
