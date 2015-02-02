# This module contains an example of code that does not work in Python 3,
# and needs to be converted with 2to3.

import StringIO

def print_something():
    out = StringIO.StringIO()
    print >> out, "This should end up in the tempfile"

def buffer_test():
    s = buffer("Whooohah")
    
def text_conversion():
    import tempfile
    binout = tempfile.TemporaryFile('w+b')
    textout = tempfile.TemporaryFile('w+t')
    binout.write("It's a string!")
    textout.write("It's a string!")
    binout.close() 
    textout.close()

