
def f(x):
    P = 5<= x <= 280
    Q = 295<= x <= 400
    R = 375 <= x <= 450
    A = a1<= x <= a2
    return ((Q<=P) or ((not A) <= R))

ox = [dx for x in (5,280,295,400,375, 450) for dx in (x-0.1, x, x+0.1)]

m = []

for a1 in ox:
    for a2 in ox:
        if a1<a2 and all(f(x)==1 for x in ox):
            m.append(a2-a1)

print(min(m))