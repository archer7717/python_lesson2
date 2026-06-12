


def f(x):
    return ((x%12==0) <= (x%42!=0)) or (x + a >= 4096)

for a in range(1, 100000):
    if all(f(x)== 1 for x in range(1, 10000)):
        print(a)
        break