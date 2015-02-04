import sys

def shouldRaise(eclass, method, *args, **kw):
    try:
        method(*args, **kw)
    except:
        e = sys.exc_info()[1]
        if not isinstance(e, eclass):
            raise
        return
    raise Exception("Expected exception %s not raised" %
                    str(eclass))
