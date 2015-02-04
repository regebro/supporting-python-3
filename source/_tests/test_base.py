# -*- coding: UTF-8 -*-
import unittest

class FixerTest(unittest.TestCase):

    def _test(self, source, target):
        refactored = str(self.refactor(source, 'zope.fixer.test'))
        if refactored != target:
            match = ''
            for i in range(min(len(refactored), len(target))):
                if refactored[i] == target[i]:
                    match += refactored[i]
                else:
                    break
            msg = "\nResult:\n" + refactored
            msg += "\nFailed:\n" + refactored[i:]
            msg += "\nTarget:\n" + target[i:]
            # Make spaces and tabs visible:
            msg = msg.replace(' ', '·')
            msg = msg.replace('\t', '------->')
            msg = ("Test failed at character %i" % i) + msg
            self.fail(msg)
