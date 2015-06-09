import re
from urllib.request import urlopen
from urllib.parse import quote
from urllib.error import HTTPError
import logging

from bs4 import BeautifulSoup

from .exception import InvalidTermException

logger = logging.getLogger(__name__)
_baseurl = 'http://www.thesaurus.com/browse/'
_regex = re.compile(r'^[A-Za-z ]+$')


def _audit(term):
    logger.debug('Checking if term "%s" is valid' % term)
    if not re.match(_regex, term):
        logger.error(('Invalid term. Only letters and white spaces are '
                      'accepted' % term))
        logger.debug('Regex: ' + _regex.pattern)
        raise InvalidTermException
    logger.debug('Valid term!')


def _fetch(url):
    logger.debug('Attempting to fetch the url: "%s"' % url)
    html = ''
    try:
        with urlopen(url) as r:
            html = str(r.read(), encoding='utf-8')
        logger.debug('Fetch succeeded!')
    except HTTPError:
        logger.error("-- NO MATCHES --")
    return html


def _parse(html):
    logger.debug('Attempting to parse HTML: %s (...)' % html[:250])
    synonyms = []
    soup = BeautifulSoup(html)
    divs = soup.find_all('div', class_='relevancy-list')
    logger.debug('divs found: %d' % len(divs))
    for d in divs:
        spans = d.find_all('span', class_='text')
        logger.debug('spans found: %s' % len(spans))
        synonyms += [s.string for s in spans]
    logger.debug('Parse succeeded!')
    return synonyms


def scrape(term):
    logger.debug(('Attempting to scrape "%s" synonyms from '
                  'http://www.thesaurus.com'))
    _audit(term)
    html = _fetch(_baseurl + quote(term))
    synonyms = _parse(html)
    logger.debug('Scrape succeeded! Found %d synonyms: %s' % (len(synonyms),
                                                              synonyms))
    return synonyms
