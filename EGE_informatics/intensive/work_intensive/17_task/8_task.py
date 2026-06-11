a = [int(x) for x in open('17-380.txt')]

b = max([x for x in a if abs(x)%100==25])

ans = []
for x,y,z in zip(a[2:], a[1:], a):
    if (1000<=abs(x)<10000) + (1000<=abs(y)<10000) + (1000<=abs(z)<10000)  <= 2 and \
            (x+y+z) <= b:
        ans.append(x+y+z)

print(len(ans), max(ans))