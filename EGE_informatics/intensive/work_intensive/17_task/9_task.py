a = [int(x) for x in open('17-426.txt')]


def check(n):
    return 10000<= abs(n) < 100000 and abs(n)%100 == 43
b = max([x for x in a if check(x)])
#print(b)
ans = []

for x,y,z in zip(a[2:], a[1:], a):
    if check(x) + check(y) + check(z) >0:
        if (x**2+y**2+z**2) <= b**2:
            ans.append(x**2+y**2+z**2)
print(len(ans), min(ans))
