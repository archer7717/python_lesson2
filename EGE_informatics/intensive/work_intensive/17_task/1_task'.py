
a = [int(x )for x in open('17-1.txt')]
ans = []
avg = sum(a)/len(a)
for x,y in zip(a, a[1:]):
    if x >avg or y>avg:
        ans.append(x+y)

print(len(ans), max(ans))
