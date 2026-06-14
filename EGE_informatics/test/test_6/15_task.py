
def f(x):
    B = 22<= x <= 40
    C = 32 <= x <= 50
    A = a1 <= x <= a2
    return (not A) <= ((B) == C)

ox = [dx for x in (22, 40, 32, 50) for dx in (x-0.1, x, x+0.1)]

m = []
for a1 in ox:
    for a2 in ox:
        if a2 > a1 and all(f(x) for x in ox):
            m.append(a2-a1)
print(min(m))