
def div(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for i in range(135743, 135790):
    s = div(i)
    if len(s)==6:
        print(s[-2], s[-1])