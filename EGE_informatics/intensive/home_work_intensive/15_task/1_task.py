
def f(x):
    P = 17 <= x <= 58
    Q = 29 <= x <=80
    A = a1<= x <= a2
    return P <= (((Q) and (not(A))) <= (not(P)))

ox = [dx for x in (17,58, 29, 80) for dx in (x-0.1, x, x+0.1)]

m = []

for a1 in ox:
    for a2 in ox:
        if a1<a2 and  all((f(x)==1 for x in ox)):
            m.append(a2-a1)

print(min(m))