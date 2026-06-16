k = 0
for s in open('9.txt'):
    #print(s)
    a = [int(x) for x in s.split()]
    if a[0] >a[1] > a[2] > a[3] > a[4] > a[5] > a[6] and (a[0] +a[6])/2 > (a[1] + a[2] + a[4] + a[5])/6:
        print(sum(a))
        break