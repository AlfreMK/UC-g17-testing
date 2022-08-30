# TEST FOR NeverReadedVariable
class Person:
    def __init__(self, firstName, lastName):
        variable_non_used_1 = 100
        self.firstName = firstName
        self.lastName = lastName

    def example_1(self):
        variable_non_used_2 = 100
        variable_used_1 = 200
        variable_used_2 = variable_used_1 + 100
        return variable_used_2
    def example_for_args(self, a, b):
        variable_used_1 = 200
        variable_used_2 = variable_used_1 + 100
        return variable_used_2
    def example_without_return(self):
        variable_used_1 = 200
        variable_non_used_3 = variable_used_1 + 100
