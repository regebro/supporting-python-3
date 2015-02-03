from shouldraise import shouldRaise
from test_fixers import IndentFixerTest, Name1FixerTest, Name2FixerTest, ConstantFixerTest
import doctest
import sys
import unittest

suite = doctest.DocFileSuite('test-1.1.txt',
                             'test-1.3.txt',
                             'test-1.4.txt',
                             'test-1.6.txt',
#                             'test-1.7.txt', Doesn't work because of a bug in doctests.
                             'test-1.8.txt',
                             'test-1.9.txt',
                             'test-1.10.txt',
                             'test-1.11.txt',
                             'test-1.12.txt',
                             'test-2.1.txt',
                             'test-2.2.txt',
                             'test-2.3.txt',
                             'test-2.4.txt',
                             'test-2.5.txt',
                             'test-3.1.txt',
                             'test-3.2.txt',
                             'test-3.3.txt',
                             'test-3.4.txt',
                             'test-3.5.txt',
                             'test-3.6.txt',
                             'test-3.7.txt',
                             'test-3.11.txt',
                             'test-3.12.txt',
                             'test-3.14.txt',
                             'test-3.15.txt',
                             'test-3.16.txt',
                             'test-3.17.txt',
                             'test-3.19.txt',
                             'test-3.20.txt',
                             'test-3.21.txt',
                             'test-3.23.txt',
                             'test-3.24.txt',
                             'test-3.25.txt',
                             'test-3.26.txt',
                             #'test-3.27.txt', Bug in doctest
                             #'test-3.28.txt', Bug in doctest
                             'test-3.29.txt',
                             'test-3.30.txt',
                             'test-4.1.txt',
                             'test-4.2.txt',
                             'test-4.3.txt',
                             'test-4.4.txt',
                             'test-4.5.txt',
                             'test-4.6.txt',
                             'test-4.7.txt',
                             'test-4.8.txt',
                             'test-4.9.txt',
                             'test-4.10.txt',
                             'test-4.11.txt',
                             'test-4.12.txt',
                             'test-4.16.txt',
                             'test-4.17.txt',
                             'test-4.18.txt',
                             'test-5.1.txt',
                             'test-5.2.txt',
                             'test-5.3.txt',
                             'test-5.4.txt',
                             'test-5.5.txt',
                             'test-5.6.txt',
                             'test-5.7.txt',
                             'test-5.9.txt',
                             'test-5.10.txt',
                             #'test-5.11.txt', Doesn't work because of a bug in doctests.
                             #'test-5.12.txt', Doesn't work because of a bug in doctests.
                             'test-5.14.txt',
                             'test-5.16.txt',
                             #'test-5.18.txt', Doesn't work because of a bug in doctests.
                             'test-6.1.txt',
                             'test-7.7.txt',
                             'test-7.11.txt',
                             'csv26.txt',
                             'upper26.txt',
                             'map26.txt',
                             optionflags=doctest.ELLIPSIS,
                             globs={'shouldRaise': shouldRaise,
                                    }
                             )

suite.addTests(unittest.makeSuite(IndentFixerTest))
suite.addTests(unittest.makeSuite(Name1FixerTest))
suite.addTests(unittest.makeSuite(Name2FixerTest))
suite.addTests(unittest.makeSuite(ConstantFixerTest))
runner = unittest.TextTestRunner()
results = runner.run(suite)

if results.failures:
    sys.exit(1)
