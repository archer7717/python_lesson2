a = [int(x) for x in open('17_1_1.txt')]


b = max([x for x in a if 10<=abs(x)<100])
ans = []
for x,y in zip(a[1:], a):
    if (10<=abs(x)<100) + (10 <= abs(y) < 100) == 1 \
            and (x+y)%b==0:
        ans.append(x+y)

print(len(ans), max(ans))