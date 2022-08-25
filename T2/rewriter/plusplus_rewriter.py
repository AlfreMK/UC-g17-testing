from . rewriter import *


class PlusPlusTransformer(NodeTransformer):
    ## El nombre visit_Assign es importante, si se coloca otro como visit_hola, no funcionara
    def visit_Assign(self, node):
        if isinstance(node, Assign):
            var = node.targets[0]
            try:
                if isinstance(node.value.op, Add):
                    if node.value.left.id == var.id and isinstance(node.value.right, Constant):
                        return AugAssign(
                                    target=Name(id=var.id, ctx=Store()),
                                    op=Add(),
                                    value=node.value.right)
            except:
                return node
        return node


class PlusPlusRewriterCommand(RewriterCommand):
    def apply(self, ast):
        new_tree = fix_missing_locations(PlusPlusTransformer().visit(ast))
        return new_tree