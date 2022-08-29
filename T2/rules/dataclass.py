from .rule import *


class VariableNodeCounterVisitor(NodeVisitor):
    def __init__(self):
        self.attrs = {}
        self.variables = []
        self.args = []

    def visit_Attribute(self, node: Attribute):
        if node.attr in self.attrs:
            self.attrs[node.attr] = self.attrs[node.attr] + 1
        else:
            self.attrs[node.attr] = 1

    def visit_Name(self, node: Name):
        self.variables.append(node.id)

    def visit_arg(self, node: arg):
        if node.arg != "self":
            self.args.append(node.arg)


class MethodNodeVisitor(NodeVisitor):
    def __init__(self):
        self.attributes = {}
        self.possibleSetterGetter = {}
        self.visited_method = 0
    
    def visit_Assign(self, node: Assign):
        if isinstance(node.targets[0], Attribute):
            self.attributes[node.targets[0].attr] = node.targets[0].attr
        NodeVisitor.generic_visit(self, node)
    
    def visit_FunctionDef(self, node: FunctionDef):
        self.visited_method += 1
        if node.name != "__init__":
            visitor = VariableNodeCounterVisitor()
            visitor.visit(node)
            for attr in visitor.attrs:
                if visitor.attrs[attr] == 1:
                    self.attributes[attr] = 1
            if node.end_lineno - node.lineno == 1:
                for var in visitor.variables:
                    if var in visitor.args:
                        self.possibleSetterGetter[self.visited_method] = 'setter'
        NodeVisitor.generic_visit(self, node)


    def visit_Return(self, node: Return):
        if isinstance(node.value, Attribute) and self.attributes[node.value.attr] == 1:
            self.possibleSetterGetter[self.visited_method] = 'getter'
        NodeVisitor.generic_visit(self, node)



class DataClassVisitor(WarningNodeVisitor):
    def __init__(self):
        super().__init__()
        self.attributes = {}
        self.possibleSetterGetter = {}
    
    def visit_ClassDef(self, node: ClassDef):
        visitor = MethodNodeVisitor()
        visitor.visit(node)
        if visitor.visited_method - 1 == len(visitor.possibleSetterGetter):
            self.addWarning('DataClass', node.lineno, 'class ' + node.name + ' is a dataclass')
        NodeVisitor.generic_visit(self, node)
    

class DataClassRule(Rule):
    def analyze(self, ast):
        visitor = DataClassVisitor()
        visitor.visit(ast)
        return visitor.warningsList()
