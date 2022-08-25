class Person:

    def __init__(self, firstName, lastName):
        self.a = firstName
        self.b = lastName

    def lenName(self):
        c = len(self.a) + len(self.b)
        return c