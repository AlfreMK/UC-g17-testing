
x = 15

if x > 10:
    x = x + 1
else:
    pass


def PlusPlus(x):
    if x > 10:
        x = x + 1
    else:
        pass
    return x

def PlusPlusExtra(y):
    if y > 2:
        if y > 3:
            y = y + 1
            if y > 4:
                y = y + 1
            else:
                pass
        else:
            pass
    else:
        pass
    return y

y = 3

if y > 2:
    y += 1
elif y == 2:
    y = y + 1
else:
    y += 1