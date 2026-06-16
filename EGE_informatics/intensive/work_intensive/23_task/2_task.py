def f(c, e):
    if c > e:
        return 0
    if c == e:
        return 1
    return f(c)