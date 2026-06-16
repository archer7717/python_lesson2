k = 0


for s in open('9.txt'):
    a = sorted([int(x) for x in s.split()])
    if a[3] < a[0] + a[1] + a[2]:
        if a[3]+a[0] == a[1] + a[2]:
            k+=1
print(k)
