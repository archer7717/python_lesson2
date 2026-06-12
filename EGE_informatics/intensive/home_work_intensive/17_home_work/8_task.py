a = [int(x) for x in open('17_8_1.txt')]

b = max(x for x in a if x%22==0)
ans = []

for x,y in zip(a[1:], a):
    if (x>b) + (y>b) >=1:
        ans.append(x+y)
print(len(ans), min(ans))