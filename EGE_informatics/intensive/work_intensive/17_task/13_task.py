a = [int(x) for x in open('17_23952.txt')]

b = max(x for x in a if abs(x)%100==93)

ans = []

for x,y in zip(a, a[1:]):
    if (x>b) + (y>b) ==1 and (str(x)[0] == '9' or str(y)[0] == '9'):
        if x > b:
            ans.append(x)
        else:
            ans.append(y)

print(len(ans), sum(ans))
