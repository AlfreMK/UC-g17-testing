from . rewriter import *


class PlusPlusTransformer(NodeTransformer):
    def visit_Assign(self, node):
        if isinstance(node, Assign):
            var = node.targets[0]
            if isinstance(node.value.op, Add):
                if node.value.left.id == var.id and isinstance(node.value.right, Constant):
                    return AugAssign(
                                target=Name(id=var.id, ctx=Store()),
                                op=Add(),
                                value=node.value.right)
        return node


class PlusPlusRewriterCommand(RewriterCommand):
    def apply(self, ast):
        new_tree = fix_missing_locations(PlusPlusTransformer().visit(ast))
        return new_tree