

def f(x):
    P = 15 <= x <= 142
    Q = 38 <= x <= 167
    A = a1 <= x <= a2
    return not (Q <=((not A and P)<=(not Q)))

ox = [dx for x in (15, 142, 38 ,167) for dx in (x-0.1, x , x+0.1)]

m = []

for a1 in ox:
    for a2 in ox:
        if a2 > a1 and all(f(x)== 0 for x in ox):
            m.append(a2-a1)

print(min(m))