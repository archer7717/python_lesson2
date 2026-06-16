

def f(c, e):
    if c> e:
        return 0
    if c == e:
        return 1
    return f(c+3,e) + f(c*2, e)

print(f(3,27)*f(27,63))