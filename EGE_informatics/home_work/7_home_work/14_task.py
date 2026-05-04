
def f(x):
    P = 10 <=x<= 29
    Q = 13<=x<=18
    A = a1 <=x <=a2
    return( A <= P) or Q
ox = [dx for x in (10,29,13,18) for dx in (x, x-0.0001, x+0.00001)]

m = []

for a1 in ox:
    for a2 in ox:
        if a2 >= a1 and all(f(x)==1 for x in ox):
            m.append(a2-a1)
print(max(m))
