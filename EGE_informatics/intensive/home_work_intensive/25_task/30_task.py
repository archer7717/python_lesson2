def p(x):
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return [i]+p(x//i)
    return [x]

for x in range(23_600_001, 25_700_000):
    d = sorted(set(p(x)))
    if len(d) >0:
        M = max(d) + min(d)
        if M%213==171:
            print(x, M)