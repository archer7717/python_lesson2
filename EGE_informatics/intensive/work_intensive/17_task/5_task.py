a = [int(x) for x in open('17-403.txt')]

minn = min(a)

ans = []
for x,y in zip(a,a[1:]):
    if x%18+y%18==minn:
        ans.append(x+y)

print(len(ans), max(ans))