import sys
if sys.version < '3':
    class Bites(str):
        def __new__(cls, value):
            if isinstance(value[0], int):
                # It's a list of integers
                value = ''.join([chr(x) for x in value])
            return super(bites, cls).__new__(cls, value)
            
        def itemint(self, index):
            return ord(self[index])
        
        def iterint(self):
            for x in self:
                yield ord(x)
else:

    class Bites(bytes):
        def __new__(cls, value):
            if isinstance(value, str):
                # It's a unicode string:
                value = value.encode('ISO-8859-1')
            return super(bites, cls).__new__(cls, value)

        def itemint(self, x):
            return self[x]
        
        def iterint(self):
            for x in self:
                yield x
 