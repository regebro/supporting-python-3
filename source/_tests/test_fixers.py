# -*- coding: UTF-8 -*-

from lib2to3.refactor import RefactoringTool
from test_base import FixerTest

# Check that various import syntaxes get renamed properly.
indent_source = """
class Klas(object):
   '''Only the first line
      of docstrings and other strings
      are touched.
   '''

   # Do some code in the class construction:
   for x in range(10):
      print x

# Comments are left alone.

   def __init__(self):
       def function(): # Ugly place for a comment
          if False:
             # This comment is unaligned
           a = 1
	   b = 2.0
           c = 0x3
          elif True:
              x = "Four"; y = "Five"
              # Hepp!
              z = 6
          else:
	           q = 'Huh?'
"""

indent_target = """
class Klas(object):
    '''Only the first line
      of docstrings and other strings
      are touched.
   '''

   # Do some code in the class construction:
    for x in range(10):
        print x

# Comments are left alone.

    def __init__(self):
        def function(): # Ugly place for a comment
            if False:
             # This comment is unaligned
                a = 1
                b = 2.0
                c = 0x3
            elif True:
                x = "Four"; y = "Five"
              # Hepp!
                z = 6
            else:
                q = 'Huh?'
"""

class IndentFixerTest(FixerTest):

    def setUp(self):
        self.refactor = RefactoringTool(['fix_indent']).refactor_string

    def test_indent(self):
        self._test(indent_source, indent_target)

# Check that various import syntaxes get renamed properly.
name_source = """from foo import oldname

def afunction(alist):
    return oldname(alist)
"""

name_target = """from foo import newname

def afunction(alist):
    return newname(alist)
"""

class Name1FixerTest(FixerTest):

    def setUp(self):
        self.refactor = RefactoringTool(['fix_name1']).refactor_string

    def test_name(self):
        self._test(name_source, name_target)


class Name2FixerTest(FixerTest):

    def setUp(self):
        self.refactor = RefactoringTool(['fix_name2']).refactor_string

    def test_name(self):
        self._test(name_source, name_target)

class Name3FixerTest(FixerTest):

    def setUp(self):
        self.refactor = RefactoringTool(['fix_name3']).refactor_string

    def test_name(self):
        self._test(name_source, name_target)

constant1_source = """import foo as bar

def afunction(alist):
    return [x*CONSTANT for x in alist]

def bfunction(blist):
    return [x*bar.CONSTANT for x in blist]
"""


constant1_target = """import foo as bar

def afunction(alist):
    return [x*CONSTANT for x in alist]

def bfunction(blist):
    return [x*bar.get_constant() for x in blist]
"""

constant2_source = """from foo import CONSTANT as renamed

def afunction(alist):
    return [x*renamed for x in alist]

def bfunction(blist):
    return [x*bar.renamed for x in blist]
"""


constant2_target = """from foo import get_constant as renamed

def afunction(alist):
    return [x*renamed() for x in alist]

def bfunction(blist):
    return [x*bar.renamed for x in blist]
"""

constant3_source = """from foo import CONSTANT

def afunction(alist):
    return [x*CONSTANT for x in alist]

def bfunction(blist):
    return [x*bar.CONSTANT for x in blist]
"""

constant3_target = """from foo import get_constant

def afunction(alist):
    return [x*get_constant() for x in alist]

def bfunction(blist):
    return [x*bar.CONSTANT for x in blist]
"""

constant1_source = """import foo

def afunction(alist):
    return [x*CONSTANT for x in alist]

def bfunction(blist):
    return [x*foo.CONSTANT for x in blist]

def cfunction(clist):
    return [x*bar.CONSTANT for x in clist]
"""


constant1_target = """import foo

def afunction(alist):
    return [x*CONSTANT for x in alist]

def bfunction(blist):
    return [x*foo.get_constant() for x in blist]

def cfunction(clist):
    return [x*bar.CONSTANT for x in clist]
"""

class ConstantFixerTest(FixerTest):

    def setUp(self):
        self.refactor = RefactoringTool(['fix_constant']).refactor_string

    def test_constant(self):
        self._test(constant1_source, constant1_target)
        self._test(constant2_source, constant2_target)
        self._test(constant3_source, constant3_target)
        self._test(open('source/_tests/constantexample.py').read(),
                   open('source/_tests/constanttarget.py').read())
