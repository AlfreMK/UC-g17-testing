class BigClass:
    
    def __init__(self, price):
        self.price = price
        
        class Element:
            def __init__(self, value):
                self.value = value
            def getValue(self):
                return self.value
            def setValue(self, value):
                self.value = value
        
        self.element_class = Element(100)
    
    def foo(self):
        print("the value of the element of the class is", self.element_class.value)
