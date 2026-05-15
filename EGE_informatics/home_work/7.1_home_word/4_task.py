def f(x):
    return ((x%4!=3) or (x%6!=1)) <= (x%36!=a)

for a in range(1,1000):
    if all(f(x)==1 for x in range(1, 1000)):
        print(a)
        break
