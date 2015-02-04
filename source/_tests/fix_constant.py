from lib2to3.fixer_base import BaseFix
from lib2to3.fixer_util import Call, Name, is_probably_builtin
from lib2to3.patcomp import PatternCompiler

class FixConstant(BaseFix):

    PATTERN = """
        import_name< 'import' modulename='foo' >
        |
        import_name< 'import' dotted_as_name< 'foo' 'as'
           modulename=any > >
        |
        import_from< 'from' 'foo' 'import'
           importname='CONSTANT' >
        |
        import_from< 'from' 'foo' 'import' import_as_name<
           importname='CONSTANT' 'as' constantname=any > >
        |
        any
        """

    def start_tree(self, tree, filename):
        super(FixConstant, self).start_tree(tree, filename)
        # Reset the patterns attribute for every file:
        self.usage_patterns = []

    def match(self, node):
        # Match the import patterns:
        results = {"node": node}
        match = self.pattern.match(node, results)

        if match and 'constantname' in results:
            # This is an "from import as"
            constantname = results['constantname'].value
            # Add a pattern to fix the usage of the constant
            # under this name:
            self.usage_patterns.append(
                PatternCompiler().compile_pattern(
                    "constant='%s'"%constantname))
            return results

        if match and 'importname' in results:
            # This is a "from import" without "as".
            # Add a pattern to fix the usage of the constant
            # under it's standard name:
            self.usage_patterns.append(
                PatternCompiler().compile_pattern(
                    "constant='CONSTANT'"))
            return results

        if match and 'modulename' in results:
            # This is a "import as"
            modulename = results['modulename'].value
            # Add a pattern to fix the usage as an attribute:
            self.usage_patterns.append(
                PatternCompiler().compile_pattern(
                "power< '%s' trailer< '.' " \
                "attribute='CONSTANT' > >" % modulename))
            return results

        # Now do the usage patterns
        for pattern in self.usage_patterns:
            if pattern.match(node, results):
                return results

    def transform(self, node, results):
        if 'importname' in results:
            # Change the import from CONSTANT to get_constant:
            node = results['importname']
            node.value = 'get_constant'
            node.changed()

        if 'constant' in results or 'attribute' in results:
            if 'attribute' in results:
                # Here it's used as an attribute.
                node = results['attribute']
            else:
                # Here it's used standalone.
                node = results['constant']
                # Assert that it really is standalone and not
                # an attribute of something else, or an
                # assignment etc:
                if not is_probably_builtin(node):
                    return None

            # Now we replace the earlier constant name with the
            # new function call. If it was renamed on import
            # from 'CONSTANT' we keep the renaming else we
            # replace it with the new 'get_constant' name:
            name = node.value
            if name == 'CONSTANT':
                name = 'get_constant'
            node.replace(Call(Name(name), prefix=node.prefix))
