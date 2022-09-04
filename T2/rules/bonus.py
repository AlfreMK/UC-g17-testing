from .rule import *


class ImportVisitor(WarningNodeVisitor):
    def __init__(self):
        self.notAllowedList = ['sys', 'numpy']
        super().__init__()

    def visit_Import(self, node: Import):
        if node.names[0].name in self.notAllowedList:
            self.addWarning('ImportWarning', node.lineno, f'{node.names[0].name} is not allowed to be imported on this homework!')
        NodeVisitor.generic_visit(self, node)


class ImportRule(Rule):
    def analyze(self, ast):
        visitor = ImportVisitor()
        visitor.visit(ast)
        return visitor.warningsList()
