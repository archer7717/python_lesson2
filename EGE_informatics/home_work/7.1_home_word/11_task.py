def f(y, x):
    return (x > 39) or (y > 26) or (2*x+ 4*y < a)

for a in range(1,1000):
    if all(f(y, x) == 1 for x in range(1, 1000) for y in range(1,1000)):
           print(a)
