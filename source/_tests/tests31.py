import unittest
import doctest
from lib2to3 import main
import shutil
import os
import sys
from test_fixers import IndentFixerTest, Name1FixerTest, Name2FixerTest, ConstantFixerTest
from shouldraise import shouldRaise

files = []
for filename in ('test-3.11.txt', 'test-4.9.txt',):
    name2 = os.path.join('source/_tests', filename)
    name3 = name2 + '.2to3'
    shutil.copy(name2, name3)
    files.append(name3)
main.main('lib2to3.fixes', args=['-d', '-w', '--no-diffs'] + files)

try:
    1/0
except ZeroDivisionError:
    traceback = sys.exc_info()[2]

suite = doctest.DocFileSuite('test-1.1.txt',
                             'test-1.3.txt',
                             'test-1.5.txt',
                             'test-1.6.txt',
                             'test-1.7.txt',
                             'test-1.12.txt',
                             'test-2.1.txt',
                             'test-2.3.txt',
                             'test-2.4.txt',
                             'test-2.5.txt',
                             'test-2.6.txt',
                             'test-3.2.txt',
                             'test-3.3.txt',
                             'test-3.5.txt',
                             'test-3.6.txt',
                             'test-3.8.txt',
                             'test-3.9.txt',
                             'test-3.10.txt',
                             'test-3.11.txt.2to3',
                             'test-3.13.txt',
                             'test-3.14.txt',
                             'test-3.15.txt',
                             'test-3.16.txt',
                             'test-3.18.txt',
                             'test-3.19.txt',
                             'test-3.20.txt',
                             'test-3.22.txt',
                             'test-3.23.txt',
                             'test-3.24.txt',
                             'test-3.25.txt',
                             'test-3.26.txt',
                             'test-3.27.txt',
                             'test-3.28.txt',
                             'test-3.29.txt',
                             'test-3.30.txt',
                             'test-3.31.txt',
                             'test-4.4.txt',
                             'test-4.5.txt',
                             'test-4.6.txt',
                             'test-4.7.txt',
                             'test-4.8.txt',
                             'test-4.9.txt.2to3',
                             'test-4.11.txt',
                             'test-5.3.txt',
                             'test-5.4.txt',
                             'test-5.5.txt',
                             'test-5.6.txt',
                             'test-5.8.txt',
                             'test-5.9.txt',
                             'test-5.13.txt',
                             'test-5.15.txt',
                             'test-5.17.txt',
                             'test-5.18.txt',
                             'test-6.2.txt',
                             'test-7.1.txt',
                             'test-7.3.txt',
                             'test-7.4.txt',
                             'test-7.5.txt',
                             'test-7.6.txt',
                             'test-7.7.txt',
                             'test-7.8.txt',
                             'test-7.9.txt',
                             'test-7.11.txt', 
                             'buffer26.txt',
                             'callable26.txt',
                             'callable30.txt',
                             'csv30.txt',
                             'dict26.txt',
                             'division26.txt',
                             'exception_syntax26.txt',
                             'exec26.txt',
                             'exec30.txt',
                             'getitem26.txt',
                             #'input26.txt', Requires input frm stdin
                             'intern26.txt',
                             'inttypes26.txt',
                             #'long26.txt', Damn doctests
                             'map26.txt',
                             'map30.txt',
                             'raise30.txt',
                             'renames26.txt',
                             'repr26.txt',
                             'unpacking26.txt',
                             'round26.txt',
                             'round30.txt',
                             'upper26.txt',
                             'unicodesort30.txt',
                             optionflags=doctest.ELLIPSIS,
                             globs={'traceback': traceback,
                                    'shouldRaise': shouldRaise,
                                    }                             
                             )

suite.addTests(unittest.makeSuite(IndentFixerTest))
suite.addTests(unittest.makeSuite(Name1FixerTest))
suite.addTests(unittest.makeSuite(Name2FixerTest))
suite.addTests(unittest.makeSuite(ConstantFixerTest))
runner = unittest.TextTestRunner()
runner.run(suite)

