def p(x):
    for i in range(2, int(x**0.5)+1):
        if x %i==0:
            return [i] + p(x//i)
    return [x]

for i in range(5_400_001, 5_409_000):
    d = sorted(set(p(i)))
    if len(d) > 0:
        M = d[0] + d[-1]
        if M > 60000 and str(M) == str(M)[::-1]:
            print(i, M)