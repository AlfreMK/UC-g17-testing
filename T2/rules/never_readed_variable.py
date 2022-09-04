from . rule import *

##############################################################################################
# ACTIVIDAD 1.2
class VariableNodeCounterVisitor(NodeVisitor):
    def __init__(self):
        self.variableOcurrences = {}
        self.variablePosition = {}

    def visit_Assign(self, node: Assign):
        if isinstance(node.targets[0], Name):
            self.variableOcurrences[node.targets[0].id] = 0
            self.variablePosition[node.targets[0].id] = node.lineno
        NodeVisitor.generic_visit(self, node)
    
    def visit_Name(self, node: Name):
        if node.id != 'self':
            if node.id not in self.variableOcurrences:
                self.variableOcurrences[node.id] = 0
            self.variableOcurrences[node.id] += 1
            self.variablePosition[node.id] = node.lineno
        NodeVisitor.generic_visit(self, node)
    
    def visit_arg(self, node: arg):  # TODO: check if args are considered as temporary variables
        if node.arg != 'self':
            self.variableOcurrences[node.arg] = 1
            self.variablePosition[node.arg] = node.lineno
        NodeVisitor.generic_visit(self, node)

class VariableMethodVisitor(WarningNodeVisitor):
    def __init__(self):
        super().__init__()
        self.variables = {}

    def visit_FunctionDef(self, node: FunctionDef):
        visitor = VariableNodeCounterVisitor()
        visitor.visit(node)
        for key in visitor.variableOcurrences:
            if visitor.variableOcurrences[key] <= 1:
                self.addWarning('NeverReadedVariable', visitor.variablePosition[key], 'variable '+ key + ' was not used')
        NodeVisitor.generic_visit(self, node)

class NeverReadedVariableRule(Rule):
    def analyze(self, ast):
        visitor = VariableMethodVisitor()
        visitor.visit(ast)
        return visitor.warningsList()

##############################################################################################