import unittest
import doctest
import sys

try:
    1/0
except ZeroDivisionError:
    traceback = sys.exc_info()[2]

suite = doctest.DocFileSuite('test-1.2.txt',
                             'test-3.5.txt',
                             'test-2.6.txt',
                             'test-3.12.txt',
                             'test-3.14.txt',
                             'test-3.15.txt',
                             'test-3.29.txt',
                             'test-4.1.txt',
                             'test-4.2.txt',
                             'test-4.3.txt',
                             'test-4.4.txt',
                             'test-4.5.txt',
                             'test-4.6.txt',
                             'test-4.7.txt',
                             'test-5.1.txt',
                             'test-5.4.txt',
                             'test-5.5.txt',
                             'buffer25.txt',
                             'buffer26.txt',
                             'callable26.txt',
                             'dict26.txt',
                             #'division26.txt', Same old bug in doctest...
                             'exceptions25.txt',
                             'exceptions25.txt',
                             'exception_syntax26.txt',
                             'exec25.txt',
                             'exec26.txt',
                             #'input26.txt', This reads from stdin, so we skip it
                             'intern26.txt',
                             'inttypes26.txt',
                             'long25.txt',
                             'long26.txt',
                             'map25.txt',
                             'raise25.txt',
                             'repr26.txt',
                             'renames26.txt',
                             'round24.txt',
                             'unpacking25.txt',
                             'unpacking26.txt',
                             'upper24.txt',
                             optionflags=doctest.ELLIPSIS,
                             globs={'traceback': traceback,
                                    }
                             )

runner = unittest.TextTestRunner()
results = runner.run(suite)

if results.failures:
    sys.exit(1)
