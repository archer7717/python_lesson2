def f(x):
    P = 2 <= x <=20
    Q = 15<=x<=25
    A = a1<=x<=a2
    return ((not A) <=  ( not P)) or Q

ox = [dx for x in (2,15,20,25) for dx in (x,x+0.1, x-0.1)]
print(ox)
m = []
for a1 in ox:
    for a2 in ox:
        if a2 >= a1 and all(f(x) == 1 for x in ox):
            m.append(a2-a1)
print(min(m))
