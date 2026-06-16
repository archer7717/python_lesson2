k = 0

for s in open('9.txt'):
    a = sorted([int(x) for x in s.split()])
    if len(set(a))==5 and a[3]+a[4] <= a[0]+a[1]+a[2]:
        k+=1
print(k)
