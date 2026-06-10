
a = [int(x) for x in open('17-282.txt')]

b = max([x for x in a if x%41==0])
ans = []
for x,y in zip(a[1:], a):
    if x+y < b:
        ans.append(x+y)
print(len(ans), max(ans))