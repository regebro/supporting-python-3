import unittest, doctest

class TestCase1(unittest.TestCase):
    
    def test_2to3(self):
        from py3example import example
        example.print_something()
        example.text_conversion()
        
    def test_bites(self):
        from py3example.bites import bites
        all = bites(range(255))
        self.assertEqual(all.itemint(25),25)
        giftag = bites('GIF89a')
        self.assertEqual([x for x in giftag.iterint()], [71, 73, 70, 56, 57, 97])
        
    def test_sorting(self):
        def dacmp(a, b):
            return cmp(a, b)
        
        dalist = [5,3,8,7,1,2,0,4,6,9]
        dalist.sort(cmp=dacmp)
        self.assertEqual(dalist, [0,1,2,3,4,5,6,7,8,9])
        
    def test_23sorted(self):
        dalist = ['ant', 'Aardvark', 'Dingo', 'banana']
        from py3example._sorted import sorted as mysort
        self.assertEqual(mysort(dalist, key=str.lower), ['Aardvark', 'ant', 'banana', 'Dingo'])
                
    def test_comparisons(self):
        from py3example.compare import ComparableMixin
        
        class Comparable(ComparableMixin):
            """This type uses ducktyping to compare"""
            def __init__(self, v):
                self.v = v
                
            def cmp_value(self):
                return self.v
            
            def __cmp__(self, other):
                try:
                    return (self.v > other.v) - (self.v < other.v)
                except AttributeError:
                    raise TypeError('Can not compare %s with %s ' % (self, other))
                
            #def _compare(self, other, method):
                #try:
                    #return getattr(self.v, method)(other.v)
                #except AttributeError:
                    #return NotImplemented
            
            #def __lt__(self, other):
                #try:
                    #return self.v < other.v
                #except AttributeError:
                    #return NotImplemented

        class InComparable(ComparableMixin):
            """These objects are not comparable with any other types"""
            def __init__(self, v):
                self.v = v
            def __cmp__(self, other):
                if not isinstance(other, InComparable):
                    raise TypeError('Can not compare InComparable and ' + type(other))
                else:
                    return (self.v > other.v) - (self.v < other.v)
                
            #def _compare(self, other, method):
                #if not isinstance(other, InComparable):
                    #return NotImplemented
                #return getattr(self.v, method)(other.v)
                
            #def __lt__(self, other):
                #print ("Incomp <")
                #if not isinstance(other, InComparable):
                    #return NotImplemented
                #else:
                    #return self.v < other.v

        incomp1 = InComparable(1)
        incomp2 = InComparable(2)
        comp1 = Comparable(1)
        comp2 = Comparable(2)
        
        self.assert_(incomp1 < incomp2)
        self.assert_(incomp2 > incomp1)
        self.assert_(incomp1 != incomp2)
        self.assert_(incomp1 == incomp1)
        self.assert_(incomp2 >= incomp1)
        self.assert_(incomp1 <= incomp2)
        
        self.assert_(comp1 < comp2)
        self.assert_(comp2 > comp1)
        self.assert_(comp1 != comp2)
        self.assert_(comp1 == comp1)
        self.assert_(comp2 >= comp1)
        self.assert_(comp1 <= comp2)
        
        self.assert_(comp1 < incomp2)
        self.assert_(comp2 > incomp1)
        self.assert_(comp1 != incomp2)
        self.assert_(comp1 == incomp1)
        self.assert_(comp2 >= incomp1)
        self.assert_(comp1 <= incomp2)
        
        self.assert_(incomp1 < comp2)
        self.assert_(incomp2 > comp1)
        self.assert_(incomp1 != comp2)
        self.assert_(incomp1 == comp1)
        self.assert_(incomp2 >= comp1)
        self.assert_(incomp1 <= comp2)
        
        # Make sure this is sortable:
        [Comparable(2), Comparable(1)].sort()
        self.assertEqual(Comparable(2) < Comparable(1), False)
        self.assertEqual(Comparable(2) > Comparable(1), True)
        # And this not:
        self.assertRaises(TypeError, [2, Comparable(1)].sort,)

def test_suite():
    suite = unittest.makeSuite(TestCase1)
    suite.addTests(doctest.DocFileSuite('README.txt', 
        optionflags=doctest.ELLIPSIS|doctest.IGNORE_EXCEPTION_DETAIL))
    return suite
