from foo import get_constant

def afunction(alist):
    return [x * get_constant() for x in alist]
