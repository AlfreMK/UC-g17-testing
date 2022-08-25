from . rule import *


class AttributeUsageVisitor(WarningNodeVisitor):
    def __init__(self):
        super().__init__()
        self.initialized = []
        self.variables = []
        self.variables_used = {}

    def visit_Assign(self, node: Assign):
        if isinstance(node.targets[0], Attribute):
            self.initialized.append(node.targets[0].attr)
        #### ACTIVIDAD 1 ####
        if isinstance(node.targets[0], Name):
            self.variables.append(node.targets[0].id)
            self.variables_used[node.targets[0].id] = False
        # print(self.initialized)
        # print(self.variables)
        #####################
        NodeVisitor.generic_visit(self, node)
    
    def visit_Attribute(self, node: Attribute):
        if self.initialized.count(node.attr) == 0:
            self.addWarning('UninitilizeAttrWarning', node.lineno, 'attribute '+ node.attr + ' was not initialized')

        #### ACTIVIDAD 1 ####
        if len(node.attr) == 1:
            self.addWarning('SuspiciousVariableName', node.lineno, 'attribute '+ node.attr + ' has only one character')
        
        NodeVisitor.generic_visit(self, node)

    def visit_Name(self, node: Name):
        if len(node.id) == 1:
            self.addWarning('SuspiciousVariableName', node.lineno, 'variable '+ node.id + ' has only one character')
        if isinstance(node.ctx, Load):
            self.variables_used[node.id] = True


    def visit_Return(self, node: Return):
        if isinstance(node.value.ctx, Load):
            self.variables_used[node.value.id] = True
        for var in self.variables:
            if self.variables_used[var] == False:
                self.addWarning('UnusedVariableWarning', node.lineno, 'variable '+ var + ' was not used')

        #####################


class UninitialiedAttributeRule(Rule):
    def analyze(self, ast):
        visitor = AttributeUsageVisitor()
        visitor.visit(ast)
        return visitor.warningsList()


#### ACTIVIDAD 1 ####
class SuspiciousVariableName(Rule):
    def analyze(self, ast):
        visitor = AttributeUsageVisitor()
        visitor.visit(ast)
        return self.warningsList
#####################