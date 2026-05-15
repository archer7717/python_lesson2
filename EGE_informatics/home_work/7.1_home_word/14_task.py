a = set(range(1,10000))

def f(x):
    P = x in {2,4,6,8,10,12,14,16,18,20}
    Q = x in {5,10, 15, 20, 25, 30, 35, 40, 45, 50}
    A = x in a
    return (A <= P) and (Q <= (not A))

for x in range(1, 10000):
    if f(x)==0:
        a.remove(x)
print(a, len(a))
