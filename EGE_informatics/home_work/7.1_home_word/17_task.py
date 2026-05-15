a = set()


def f(x):
    P = x  in {2,4,6,8,10,12,14,16,18,20}
    Q = x in {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
    R = x in {12,24, 36, 48, 60}
    A = x in a
    return (not A) <= ((((P) and Q)) <= R)
for x in range(1,10000):
    if f(x)==0:
        a.add(x)
print(a)
