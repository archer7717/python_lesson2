def div(x):
    d = set()
    for i in range(2, int((x**0.5))+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)


for i in range(799_000, 800_000):
    d = div(i)
    if d == []:
        continue
    m = max(d) + min(d)
    if m%10==2:
        print(i, m)