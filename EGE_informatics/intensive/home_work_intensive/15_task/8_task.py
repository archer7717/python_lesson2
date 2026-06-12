def f(x,y):
    return (3*x*y> a) or (x > y) or (2717 > x)


for a in range(22_150_000, 0 , -1):
    if all(f(x,y) == 1 for x in range(2717, 2800, 1) for y in range(x,2800)):
        print(a)
        break