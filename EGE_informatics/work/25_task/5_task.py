
def div(x):
    d = set()
    for i in range(2, int((x**0.5))+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for i in range(150_00,156_000):
    S = sum([i for i in div(i) ])
    if S%13==10:
        print(i, S)