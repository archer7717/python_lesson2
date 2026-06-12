

def f(x):
    P = 66 <= x <= 67
    O = 32 <= x <= 125
    T = 30 <= x <= 491
    A = a1<= x<= a2
    return (not A ) <= (P or not(O) or not(T))

ox = [dx for x in (66,67,32,125,30,391) for dx in (x-0.1, x, x+0.1)]


m = []

for a1 in ox:
    for a2 in ox:
        if a1 < a2 and all(f(x)==1 for x in ox):
            m.append(a2-a1)

print(min(m))