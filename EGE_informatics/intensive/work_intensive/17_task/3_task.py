a = [int(x) for x in open('17-243.txt')]

b = max([x for x in a if x%19==0])

ans = []

for x,y in zip(a, a[1:]):
    if x> b or y> b:
        ans.append(x+y)
print(len(ans), min(ans))