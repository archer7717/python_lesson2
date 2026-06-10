a = [int(x) for x in open('17-407.txt')]

m = len([x for x in a if abs(x)%32==0])

ans = []

for x,y in zip(a, a[1:]):
    if (x<0 or y<0) and x+y<m:
        ans.append(x+y)
print(len(ans), max(ans))