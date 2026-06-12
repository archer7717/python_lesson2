
def f(x):
    P =  15 <= x <= 33
    Q = 35<= x <= 48
    A = a1<= x <= a2
    return (A and not Q) <= (P or Q)

ox = [dx for x in (15,33,35,48) for dx in (x-0.01, x, x+0.01)]

m = []

for a1 in ox:
    for a2 in ox:
        if a2 > a1 and all(f(x) == 1 for x in ox):
            m.append(a2-a1)

print(max(m))