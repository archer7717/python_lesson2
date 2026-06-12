

def f(x):
    return ((x%a==0) and (x%37==0)) <= (x%3737==0) and  (a < 1000)

for a in range(1, 1000):
    if all(f(x)==1 for x in range(37,10**6, 37)):
        print(a)