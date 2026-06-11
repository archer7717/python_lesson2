a = [int(x) for x in open('17_28938.txt')]

mx = max([x for x in a if abs(x)%100==28])


ans = []

for x,y,z in zip(a, a[1:], a[2:]):
    if (100<= abs(x) < 1000 or 100<= abs(y) < 1000 or 100<= abs(z) < 1000  ) and \
        (x+y+z)/3>0 and (x+y+z)/3 < mx:
        ans.append((x+y+z))
print(len(ans), max(ans))