a = [int(x) for x in open('17-339.txt')]

m = min([int(x) for x in a if x>0 and x%19==0])
ans = []
for x,y in zip(a, a[1:]):
    if x+y < m:
        ans.append(x+y)
print(len(ans), max(ans))