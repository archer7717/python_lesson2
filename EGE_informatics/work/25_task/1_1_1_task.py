
def div(x):
    d = []
    for i in range(1, int(x**0.5) + 1):
        if x%i==0:
            d.append(i)
            d.append(x//i)
    return sorted(d)

for i in range(800_000_000, 800_100_000):
    