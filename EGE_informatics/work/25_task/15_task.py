

def div(x):
    d = []
    for i in range(2, int((x**0.5)) +1):
        if x % i == 0:
            d.append(i)
            d.append(x//i)
    return sorted(d)

for x in range(450_001, 451_000):
    d = div(x)
    if len(d)> 0:
        M = max(d)
        if len(div(M))>0:
            print(x, M)
