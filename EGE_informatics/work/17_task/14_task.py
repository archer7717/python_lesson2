a = [int(x) for x in open('17-426.txt')]


def check(n):
    return 1000<= abs(n) <100000 and abs(n)%100==43


m = max(x for x in a if check(x))

ans = []

for x,y,z in zip(a,a[1:],a[2:]):
    if (check(x)) or (check(y)) or (check(z))  and x**2+y**2+z**2 <= m**2:
        ans.append(x**2+y**2+z**2)
print(len(ans), min(ans))