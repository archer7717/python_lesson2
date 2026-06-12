a = [int(x) for x in open('17_2_1.txt')]

b = len([x for x in a if x%32==0])

ans = []

for x,y in zip(a[1:], a):
    if (x <0) + (y< 0) >= 1\
        and (x+y)<b:
        ans.append(x+y)
print(len(ans), max(ans))
