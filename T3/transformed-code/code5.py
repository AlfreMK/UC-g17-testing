def sum(a, b):
    Profile.record('sum', [a, b])
    return a + b
listSum = [sum(1, 1) * i for i in range(10)]