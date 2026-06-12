
def f(x):
    return ((x%10==0) and (x%26==0) and (x >= 300)) <= (a <= x)


apper = []
for x in range(1, 100000):
    if x <300 and x%10!=0 and x %26!=0:
        apper.append(x)

for a in range(1000000, 0, -1):
    if all(f(x) for x in apper):
        print(a)