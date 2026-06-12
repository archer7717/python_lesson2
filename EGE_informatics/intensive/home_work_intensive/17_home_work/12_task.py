a = [int(x) for x in open('17_12_1.txt')]

b = max(x for x in a if abs(x)%100==37)

ans = []
for x,y in zip(a[1:], a):
    if (10000<= abs(x) < 100000) + (10000<= abs(y) < 100000) == 1 \
        and (x+y)**2 >  b**2:
        ans.append(x+y)
print(len(ans), max(ans))
