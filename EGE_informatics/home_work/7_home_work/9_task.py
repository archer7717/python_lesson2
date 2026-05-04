def f(x, y):
    return (x + 2 * y > a) or (y < x) or ( x < 30)

for a in range(1000, 0, -1):
    if all(f(x,y) == 1 for x in range(0, 1000) for y in range(0, 1000)):
        print(a)
