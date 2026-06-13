

def div(x):
    d = set()
    for i in range(1, int(x**0.5) + 1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)
for x in range(135743, 135790):
    d = div(x)
    if len(d)==6:
        print(d[-2], d[-1])
