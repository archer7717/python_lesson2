

def f(x):
    P = 254<= x <= 800
    Q = 410<= x <= 823
    A = a1<= x <= a2
    return (P and not A) <= Q


ox = [dx for x in (254, 800, 410, 823) for dx in (x-0.1, x, x+0.1)]

m = []


for a1 in ox:
    for a2 in ox:
        if a1<a2 and all(f(x)==1 for x in ox):
            m.append(a2-a1)

print(min(m))