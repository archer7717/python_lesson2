k = 0

for s in open('9.txt'):
    a = [int(x) for x in s.split()]
    a = sorted(a)
    if (a[0]+a[4])**2> a[1]**2+a[2]**2+a[3]**2:
        k+=1
print(k)

