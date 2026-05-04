

def f(x):
    B = 36<= x<= 75
    C = 60 <=x<=110
    A = a1 <= x<=a2
    return ( not A) <= (B == C)

ox = [dx for x in (36,75,60,110) for dx in (x, x+0.0001, x-0.0001)]

m =[]

for a1 in ox:
    for a2 in ox:
        if a2 >= a1 and all(f(x)==1 for x in ox):
            m.append(a2-a1)

print(min(m))
