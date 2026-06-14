
def div(x):
    d = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)

for x in range(200_000_001, 200_001_000):
    d =div(x)
    if len(d) >= 5:
        P = d[0]*d[1]*d[2]*d[3]*d[4]
        if P%10 == 1 and P<= x:
            print(P, d[4])