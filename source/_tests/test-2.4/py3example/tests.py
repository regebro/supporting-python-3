import unittest, doctest
import StringIO

class TestCase1(unittest.TestCase):
    
    def test_2to3(self):
        out = StringIO.StringIO()
        print >> out, "This should end up in the tempfile"
    
def test_suite():
    suite = unittest.makeSuite(TestCase1)
    return suite
