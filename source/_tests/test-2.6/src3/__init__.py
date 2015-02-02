import sys
print("This should not work in Python 2", file=sys.stderr)

try:
    readme = open('docs/README.txt', 'rt').read()
    changes = open('docs/CHANGES.txt', 'rt').read()
except IOError as e:
    readme = ""
    changes = ""
