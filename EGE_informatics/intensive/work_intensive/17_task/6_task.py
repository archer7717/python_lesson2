a = [int(x) for x in open('17_25356.txt')]


b = max([x for x in a if abs(x)%100==30])

ans = []
for x,y,z in zip(a[2:], a[1:], a):
    if not(1000<= abs(x) < 10000) and  not(1000<= abs(y) < 10000) and not(1000<= abs(z) < 10000)  \
        and (x+y+z)> b:
        ans.append(x+y+z)

print(len(ans), max(ans))