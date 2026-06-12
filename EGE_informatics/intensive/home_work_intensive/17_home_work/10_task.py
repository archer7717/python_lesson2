a = [int(x) for x in open('17_10_1.txt')]

b = min(x for x in a if x >0 and x%35==0)

ans = []
for x,y in zip(a[1:], a):
    if x!=y and abs(x-y)%b==0:
        ans.append(x+y)

print(len(ans), max(ans))