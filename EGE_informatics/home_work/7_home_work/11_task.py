
def poz(n, m):
    return n-m>0


def f(x,y):
    return not poz(x+y, 73) or not poz(37, x-y) or poz(y, a)

for a in range(1000,1, -1):
    if all(f(x,y)==1 for x in range(1, 1000) for y in range(1,1000)):
        print(a)
