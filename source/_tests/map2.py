from itertools import starmap, zip_longest

def map(func, *iterables):
    zipped = zip_longest(*iterables)
    if func is None:
        # No need for a NOOP lambda here
        return zipped
    return starmap(func, zipped)
