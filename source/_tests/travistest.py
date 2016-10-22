import sys

version = '%s%s' % (sys.version_info[0], sys.version_info[1])
testfile = 'tests' + version + '.py'
with open(testfile, 'rb') as f:
    exec(f.read())
