from lib2to3.fixer_base import BaseFix
from lib2to3.fixer_util import Leaf
from lib2to3.pgen2 import token

class FixIndent(BaseFix):
    
    indents = []
    line = 0
    
    def match(self, node):
        if isinstance(node, Leaf):
            return True
        return False

    def transform(self, node, results):
        if node.type == token.INDENT:
            self.line = node.lineno
            # Tabs count like 8 spaces.
            indent = len(node.value.replace('\t', ' ' * 8))
            self.indents.append(indent)
            # Replace this indentation with 4 spaces per level:
            new_indent = ' ' * 4 * len(self.indents)
            if node.value != new_indent:
                node.value = new_indent
                # Return the modified node:
                return node
        elif node.type == token.DEDENT:
            self.line = node.lineno
            if node.column == 0:
                # Complete outdent, reset:
                self.indents = []
            else:
                # Partial outdent, we find the indentation
                # level and drop higher indents.
                level = self.indents.index(node.column)
                self.indents = self.indents[:level+1]
                if node.prefix:
                    # During INDENT's the indentation level is
                    # in the value. However, during OUTDENT's
                    # the value is an empty string and then
                    # indentation level is instead in the last
                    # line of the prefix. So we remove the last
                    # line of the prefix and add the correct
                    # indententation as a new last line.
                    prefix_lines = node.prefix.split('\n')[:-1]
                    prefix_lines.append(' ' * 4 * 
                                        len(self.indents))
                    new_prefix = '\n'.join(prefix_lines)
                    if node.prefix != new_prefix:
                        node.prefix = new_prefix
                        # Return the modified node:
                        return node
        elif self.line != node.lineno:
            self.line = node.lineno
            # New line!
            if not self.indents:
                # First line. Do nothing:
                return None
            else:
                # Continues the same indentation
                if node.prefix:
                    # This lines intentation is the last line
                    # of the prefix, as during DEDENTS. Remove
                    # the old indentation and add the correct
                    # indententation as a new last line.
                    prefix_lines = node.prefix.split('\n')[:-1]
                    prefix_lines.append(' ' * 4 * 
                                        len(self.indents))
                    new_prefix = '\n'.join(prefix_lines)
                    if node.prefix != new_prefix:
                        node.prefix = new_prefix
                        # Return the modified node:
                        return node                    

        # Nothing was modified: Return None
        return None
