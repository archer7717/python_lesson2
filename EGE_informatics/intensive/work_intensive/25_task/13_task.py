
def p(x):
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return [i] + p(x//i)
    return [x]

for x in range(250_001, 251_000):
    d = sorted(set(p(x)))

    if d[0]!=x:
        S = sum(d)
        if S%17==0:
            print(x, S)