def generatorFunction(name):
    def Example(stringToPrint):
        print(stringToPrint)
    Example(name)
    Example(name)
    return Example

generatorFunction("Hello")