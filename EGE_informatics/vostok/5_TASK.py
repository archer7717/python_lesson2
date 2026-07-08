def f(x, end):
    if x > end:
        return 0
    if x == end:
        return 1
    h = []
    h.append(f(x+3, end))
    if len(str(x)) == 2:
        x = str(x)
        if x[0] < x[1]:
            h.append(f(int(x[1] + x[0]), end))

    if len(str(x)) == 3:
        x = str(x)
        if x[1] < x[2]:
            h.append((f(int(x[0]+ x[2]+x[1]), end)))
    return sum(h)
print(f(10, 169))