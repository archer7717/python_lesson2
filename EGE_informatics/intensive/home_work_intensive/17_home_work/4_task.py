a = [int(x) for x in open('17_4_1.txt') ]

b = max(x**2 for x in a if abs(x)%100==12)

ans = []


for x,y, in zip(a[1:], a):
    if (x%100==12) + (y%100==12) == 1:
        if (x+y)**2 < b:
            ans.append(x+y)
print(len(ans), max(ans))