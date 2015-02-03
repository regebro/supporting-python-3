from shouldraise import shouldRaise
import doctest
import sys
import unittest

suite = doctest.DocFileSuite('test-4.19.txt',
                             optionflags=doctest.ELLIPSIS,
                             globs={'shouldRaise': shouldRaise,
                                    }
                             )

runner = unittest.TextTestRunner()
results = runner.run(suite)

sys.exit(1 if results.failures else 0)
