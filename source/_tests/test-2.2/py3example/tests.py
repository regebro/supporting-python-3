import unittest, doctest, StringIO

class TestCase1(unittest.TestCase):
    
    def test_2to3(self):
        assert True
    
def test_suite():
    suite = unittest.makeSuite(TestCase1)
    return suite
