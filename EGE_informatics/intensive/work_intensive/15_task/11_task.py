def f(x, y):
    return (x + 2*y > a) or (y<x) or (x<30)


for a in range(1, 10000):
    if all(f(x, y)==1  for x in range(30, 100) for y in range(x, x+100)):
        print(a)