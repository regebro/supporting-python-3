import unittest
import doctest
import types
import sys

# Having them all in one suite doesn't work in Python 2.3.
for testfile in ['test-3.6.txt',
                 'test-3.11.txt',
                 'test-3.12.txt',
                 'test-4.7.txt',
                 'test-5.4.txt',
                 'test-5.5.txt',
                 'test-7.10.txt',
                 ]:
    test = open('source/_tests/' + testfile).read()
    mod = types.ModuleType('testmodule')
    mod.__doc__ = test
    mod.__file__ = ''
    sys.modules['testmodule'] = mod

    suite = doctest.DocTestSuite('testmodule')

    runner = unittest.TextTestRunner()
    runner.run(suite)

del sys.modules['testmodule']
