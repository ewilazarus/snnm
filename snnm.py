#!/usr/bin/python

"""
snnm
~~~~

This module contains the source code for `snnm`

Snnm is an utility tool created to fetch synonyms for a given expression from
the web and print them to the console.
"""
import bs4
import click
import requests

BASE_URL = 'http://www.thesaurus.com/browse/'


def _fetch_html(expression):
    """
    Returns the HTML containing the synonyms for the given expression
    """
    response = requests.get(BASE_URL + expression)
    response.raise_for_status()
    return response.text


def _parse_html(html):
    """
    Returns a parsed list of synonyms out of a given HTML
    """
    parser = bs4.BeautifulSoup(html, 'html.parser')

    synonyms = []
    divs = parser.find_all('div', class_='relevancy-list')
    for div in divs:
        spans = div.find_all('span', class_='text')
        synonyms += [str(span.string) for span in spans]
    return synonyms


def fetch_synonyms(expression):
    """
    Returns a list of synonyms for a given expression
    """
    try:
        return _parse_html(_fetch_html(expression))
    except requests.exceptions.HTTPError:
        return []


def clean(synonyms):
    """
    Returns the deduped, sorted list of synonyms
    """
    deduped_synonyms = list(set([s.strip() for s in synonyms]))
    deduped_synonyms.sort()
    return deduped_synonyms


def print_synonyms_ugly(synonyms):
    """
    Prints the list of synonyms to the screen
    """
    for synonym in synonyms:
        print(synonym)


def print_synonyms(synonyms):
    """
    Prints the list of synonyms to the screen, using colors and breakpoints
    """
    if not synonyms:
        click.secho('-- NO RESULTS --', fg='red')
        click.echo()
    else:
        height = click.get_terminal_size()[1] - 3
        batch = [synonyms[i:i+height] for i in range(0, len(synonyms), height)]
        for synonyms in batch:
            for synonym in synonyms:
                click.secho(synonym, fg='yellow')
            click.echo()
            if batch.index(synonyms) != len(batch) - 1:
                click.echo('Press any key to continue ...', nl=False)
                key = click.getchar()
                if key == '\x03':
                    raise KeyboardInterrupt()
                click.echo()


@click.command(name='snnm')
@click.argument('expression')
@click.option('-u', '--ugly-output', is_flag=True)
def main(expression, ugly_output):
    """
    List synonyms for an expression
    """
    try:
        if not ugly_output:
            click.echo('Synonyms for {}:'.format(click.style(expression,
                                                             fg='blue')))

        synonyms = clean(fetch_synonyms(expression))
        if ugly_output:
            print_synonyms_ugly(synonyms)
        else:
            print_synonyms(synonyms)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
