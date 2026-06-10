a = [int(x ) for x in open('17-338.txt')]

b = min(a)

ans = []
for x,y in zip(a[1:], a):
    if x%117==b or y%117==b:
        ans.append(x+y)
print(len(ans), max(ans))