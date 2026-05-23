def f(x):
    return (x%15 and x%10!=0) <= (a < x + 50)

for a in range(1, 1000):
    if all(f(x) == 1 for x in range(1, 100000)):
        print(a)

