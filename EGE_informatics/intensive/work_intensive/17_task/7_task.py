a = [int(x) for x in open('17-408.txt')]

b = max([x for x in a if abs(x)%10==3 and 100<= abs(x) < 1000])
ans = []
for x,y,z in zip(a[2:], a[1:], a):
    if ((100<= abs(x) <1000 and abs(x)%10==3) or (100<= abs(y) <1000 and abs(y)%10==3) or (100<= abs(z) <1000 and abs(z)%10==3)) \
        and ((x+y+z) < b):
        ans.append(x+y+z)
print(len(ans), max(ans))