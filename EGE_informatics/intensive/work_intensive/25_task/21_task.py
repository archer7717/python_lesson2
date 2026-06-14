

def p(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return [i]+p(x//i)
    return [x]


def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return [1] + sorted(d)

for k in range(1, 10000):
    x = 500_000_000 + k
    d = p(x)
    if len(d) < 3:
        print(k, max(div(x)))