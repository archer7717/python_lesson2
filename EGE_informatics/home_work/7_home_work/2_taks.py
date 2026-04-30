def f(x):
    return ( x%12==0) <= (x%90!=0) or (x + 2*a >= 512)

for a in range(1, 100000):
    if all(f(x)==1 for x in range(1, 1000000)):
        print(a)

