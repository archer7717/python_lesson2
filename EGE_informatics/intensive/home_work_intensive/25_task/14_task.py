def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(150001, 160000):
    d = div(x)
    if len(d) >0:
        S = sum(x for x in d)
        if S%13==10:
            print(x, S)