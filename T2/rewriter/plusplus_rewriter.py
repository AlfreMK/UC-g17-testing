from . rewriter import *

# variable = variable + x
# variable = x + variable
###########################
# variable += x
###########################

class PlusPlusTransformer(NodeTransformer):
    def visit_Assign(self, node):
        if isinstance(node, Assign):
            var = node.targets[0]
            try:
                if isinstance(node.value.op, Add):
                    if isinstance(node.value.left, Name):
                        if node.value.left.id == var.id:
                            return AugAssign(
                                        target=Name(id=var.id, ctx=Store()),
                                        op=Add(),
                                        value=node.value.right)
                    elif isinstance(node.value.right, Name):
                        if node.value.right.id == var.id:
                            return AugAssign(
                                    target=Name(id=var.id, ctx=Store()),
                                    op=Add(),
                                    value=node.value.left)
            except AttributeError:
                pass
            try:
                if isinstance(node.value, BinOp):
                    if node.value.left.value.id == "self":
                        return AugAssign(
                            target=Attribute(
                            value=Name(id='self', ctx=Load()),
                            attr='value',
                            ctx=Store()),
                            op=Add(),
                            value=node.value.right)
                elif isinstance(node.value.right, Name):
                        if node.value.right.id == var.id:
                            return AugAssign(
                                    target=Name(id=var.id, ctx=Store()),
                                    op=Add(),
                                    value=node.value.left)
            except AttributeError:
                pass
        return node


class PlusPlusRewriterCommand(RewriterCommand):
    def apply(self, ast):
        new_tree = fix_missing_locations(PlusPlusTransformer().visit(ast))
        return new_tree