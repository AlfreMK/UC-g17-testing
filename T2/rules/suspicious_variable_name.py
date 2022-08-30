from . rule import *

class AttributeUsageVisitor(WarningNodeVisitor):

    def visit_Attribute(self, node: Attribute):
        if len(node.attr) == 1:
            self.addWarning('SuspiciousVariableName', node.lineno, 'attribute '+ node.attr + ' has only one character')
        
        NodeVisitor.generic_visit(self, node)

    def visit_Name(self, node: Name):
        if len(node.id) == 1:
            self.addWarning('SuspiciousVariableName', node.lineno, 'variable '+ node.id + ' has only one character')

class SuspiciousVariableName(Rule):
    def analyze(self, ast):
        visitor = AttributeUsageVisitor()
        visitor.visit(ast)
        return visitor.warningsList()