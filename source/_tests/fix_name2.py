from lib2to3.fixer_base import BaseFix
from lib2to3.fixer_util import Name

class FixName2(BaseFix):

    PATTERN = "fixnode='oldname'"

    def transform(self, node, results):
        fixnode = results['fixnode']
        fixnode.replace(Name('newname', prefix=fixnode.prefix))
