import unittest
import doctest
from shouldraise import shouldRaise

suite = doctest.DocFileSuite('test-4.19.txt', 
                             optionflags=doctest.ELLIPSIS,
                             globs={'shouldRaise': shouldRaise,
                                    }                             
                             )

runner = unittest.TextTestRunner()
runner.run(suite)
