def f(x, y):
    return ((x*y) < 3*a) or (x >= 31) or (x <5*y)

for a in range(1, 10000):
    if all(f(x, y)==1 for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
