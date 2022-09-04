def generatorFunction(name):
    Profile.record('generatorFunction', [name])

    def Example(stringToPrint):
        Profile.record('Example', [stringToPrint])
        print(stringToPrint)
    Example(name)
    Example(name)
    return Example
generatorFunction('Hello')