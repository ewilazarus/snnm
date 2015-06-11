import os
import shelve
from functools import wraps

_cachepath = os.path.join(os.path.dirname(__file__), 'snnm.cache')


def cached(f):
    @wraps(f)
    def wrapper(term):
        result = None
        cache = shelve.open(_cachepath)
        if term in cache:
            result = cache[term]
        else:
            result = f(term)
            cache.clear()
            cache[term] = result
        cache.close()
        return result
    return wrapper
