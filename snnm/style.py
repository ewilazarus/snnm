import re
import unicodedata

import logging
logger = logging.getLogger(__name__)


def _camel(sentence):
    rv = ''
    words = sentence.split()
    for w in words:
        rv += w.title()
    return rv


def _mixed(sentence):
    words = sentence.split()
    rv = words[0].lower()
    if len(words) > 1:
        rv += _camel(' '.join(words[1:]))
    return rv


def _underscore(sentence):
    rv = sentence.lower()
    rv = rv.replace(' ', '_')
    return rv


def _constant(sentence):
    return _underscore(sentence).upper()


_action = {
    'mixed': _mixed,
    'camel': _camel,
    'underscore': _underscore,
    'constant': _constant,
}


def _normalize(word):
    w = word.strip()
    w = re.sub(r'\s+', ' ', w)
    w = re.sub(r'[^\d\w\s]+', '', w)
    w = unicodedata.normalize('NFKD', w)
    w = w.encode('ascii', 'ignore').decode('utf-8')
    return w


def adorn(words, style):
    if style:
        logger.debug('Stylizing synonyms in a %s fashion' % style)
        adorned = []
        for w in words:
            nw = _normalize(w)
            adorned.append(_action[style](nw))
        return adorned
    return words
