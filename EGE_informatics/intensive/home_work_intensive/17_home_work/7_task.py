a = [int(x) for x in open('17_7_1.txt')]

b = sum(a)/len(a)

ans = []

for x,y in zip(a[1:], a):
    if x<b and y < b \
        and (x%10==9) + (y%10==9) >=1:
        ans.append(x+y)

print(len(ans), max(ans))