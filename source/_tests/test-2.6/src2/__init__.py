import sys
print >> sys.stderr, "This should not work in Python 3"

try:
    readme = open('docs/README.txt', 'rt').read()
    changes = open('docs/CHANGES.txt', 'rt').read()
except IOError, e:
    readme = ""
    changes = ""
