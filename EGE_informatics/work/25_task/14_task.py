def fact(x):
    d = []
    i = 2
    while i**2 <= x:
        while x % i == 0:
            d.append(i)
            x = x // i
        i += 1
    if x > 1:
        d.append(x)
    return d

for x in range(23_600_001, 23_700_000):
    d = [i for i in fact(x) if i != x]
    if len(d) > 0:
        M = max(d) + min(d)
        if M % 213 == 171:
            print(x, M)