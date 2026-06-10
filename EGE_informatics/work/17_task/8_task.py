a = [int(x) for x in open('17-243.txt')]


maxx = 0

for x in a:
    if x%71==0:
        if x > maxx:
            maxx = x

ans = []
for x, y in zip(a, a[1:]):
    if x < maxx and y < maxx:
        if x%13==0 or y%13==0:
            ans.append(x+y)
print(len(ans), min(ans))