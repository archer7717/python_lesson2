def f(x):
    return ((x%3!=0) or (x%5!=0)) or (a >= 42 - x)

for a in range(1, 100000):
    if all(f(x) == 1 for x in range(1, 100000)):
        print(a)