
def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x %i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)


for i in range(550001, 560001):
    d = [x for x in div(i) if x % 10 == 7]
    if len(d) > 0:
        if len(d)==3:
            print(i, max(d))


