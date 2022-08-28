from .rule import *


class ImportVisitor(WarningNodeVisitor):
    def __init__(self):
        self.notAllowedList = ['sys', 'numpy']
        self.allowedImport = ['math']
        self.onlyAllowMethod = ['log', 'exp']
        super().__init__()

    def visit_Import(self, node: Import):
        if node.names[0].name in self.notAllowedList:
            self.addWarning('ImportWarning', node.lineno, f'{node.names[0].name} is not allowed to be imported on this homework!')
        NodeVisitor.generic_visit(self, node)
    
    def visit_Attribute(self, node: Attribute):
        if node.value.id in self.allowedImport:
            if not (node.attr in self.onlyAllowMethod):
                self.addWarning('ImportWarning', node.lineno, f'{node.value.id}.{node.attr} is not allowed to be imported on this homework!')
        else:
            self.addWarning('ImportWarning', node.lineno, f'{node.value.id} is not allowed to be imported on this homework!')
        NodeVisitor.generic_visit(self, node)



class ImportRule(Rule):
    def analyze(self, ast):
        visitor = ImportVisitor()
        visitor.visit(ast)
        return visitor.warningsList()
