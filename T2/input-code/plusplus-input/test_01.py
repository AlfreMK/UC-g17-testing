def PlusPlus(x):
    x = 5 + x
    x = x + 5
    y = 5
    x = x + y
    x += 5
    return x

class Element:
    def __init__(self, value):
        self.value = value
    def PlusPlus(self):
        self.value = self.value + 1