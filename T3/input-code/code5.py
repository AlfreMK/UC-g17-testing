def sum(a,b):
    return a + b

listSum = [sum(1, 1)*i for i in range(10)]

## Code is equivalent to:
# listSum = []
# for i in range(10):
#     listSum.append(sum(1, 1)*i)