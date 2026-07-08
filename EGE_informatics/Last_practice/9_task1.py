
k = 0
for s in open('9.txt'):
    a = sorted([int(x) for x in s.split()])
    k+=1
    if a[0] + a[-1] == a[1]+a[2]+a[3]:
        print(k, sum(a))

print(1037-179)