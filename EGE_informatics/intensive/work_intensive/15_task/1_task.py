def f(x):
    return (x%128==0) <= ((x%a!=0)  <= (x%80!=0))

for a in range(1, 100_000):
    if all(f(x)==1 for x in range(1, 10000)):
        print(a)

