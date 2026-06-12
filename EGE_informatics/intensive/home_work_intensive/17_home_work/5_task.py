a=  [int(x) for x in open('17_5_1.txt')]

b = min(x for x in a )
ans = []

for x,y in zip(a[1:], a):
    if (x%117==b) + (y%117==b) >=1:
        ans.append(x+y)
print(len(ans), max(ans))