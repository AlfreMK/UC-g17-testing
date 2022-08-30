from . rewriter import *


class IfWithoutElseTransformer(NodeTransformer):
    ## El nombre visit_If es importante, si se coloca otro como visit_Else, no funcionara
    def visit_If(self, node):
        NodeTransformer.generic_visit(self, node)
        if isinstance(node, If):
            if len(node.orelse) == 1 and isinstance(node.orelse[0], Pass):
                node.orelse = []
                return node
        return node


class IfWithoutElseRewriterCommand(RewriterCommand):
    def apply(self, ast):
        new_tree = fix_missing_locations(IfWithoutElseTransformer().visit(ast))
        return new_tree