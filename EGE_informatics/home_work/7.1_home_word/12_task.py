def f(x, y):
    return (2*x+y !=70) or (x < y) or (a < x)
for a in range(1,1000):
    if all(f(x,y)==1 for x in range(1,1000) for y in range(1,1000)):
        print(a)

