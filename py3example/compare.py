class ComparableMixin2(object):
    def __ne__(self, other): 
        print (">=")
        return other < self or self < other
    def __eq__(self, other): 
        print ("==")
        return not self != other
    def __gt__(self, other): 
        print (">")
        return other < self
    def __ge__(self, other): 
        print (">=")
        return not (self < other)
    def __le__(self, other): 
        print ("<=")
        return not (self > other)
    
class ComparableMixin3(object):
    def __lt__(self, other):
        try:
            return self.__cmp__(other) < 0
        except TypeError:
            return NotImplemented
        
    def __le__(self, other):
        try:
            return self.__cmp__(other) <= 0
        except TypeError:
            return NotImplemented

    def __gt__(self, other):
        try:
            return self.__cmp__(other) > 0
        except TypeError:
            return NotImplemented

    def __ge__(self, other):
        try:
            return self.__cmp__(other) >= 0
        except TypeError:
            return NotImplemented

    def __eq__(self, other):
        try:
            return self.__cmp__(other) == 0
        except TypeError:
            return NotImplemented

    def __ne__(self, other): 
        try:
            return self.__cmp__(other) != 0
        except TypeError:
            return NotImplemented

class ComparableMixin(object):
    def _compare(self, other, values):
        try:
            return self.__cmp__(other) in values
        except TypeError:
            return NotImplemented

    def __lt__(self, other): return self._compare(other, (-1,))
        
    def __le__(self, other): return self._compare(other, (-1, 0,))

    def __eq__(self, other): return self._compare(other, (0,))

    def __ge__(self, other): return self._compare(other, (0, 1,))

    def __gt__(self, other): return self._compare(other, (1,))

    def __ne__(self, other): return self._compare(other, (-1, 1,))


class ComparableMixin4(object):
    def __lt__(self, other):
        return self._compare(other, '__lt__')
        
    def __le__(self, other):
        return self._compare(other, '__le__')

    def __gt__(self, other):
        return self._compare(other, '__gt__')

    def __ge__(self, other):
        return self._compare(other, '__ge__')

    def __eq__(self, other):
        return self._compare(other, '__eq__')

    def __ne__(self, other): 
        return self._compare(other, '__ne__')
        