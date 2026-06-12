a = [int(x) for x in open('17_3_1.txt')]

b = min(x for x in a)
ans = []

for x,y in zip(a[1:], a):
    if x%77 + y%77 == b:
        ans.append(x+y)
print(len(ans), max(ans))