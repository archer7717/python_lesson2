
def to10(a, n):
    a = a[::-1]
    s = 0
    for i in range(len(a)):
        s = s + a[i]*n**i
    return s

for p in range(10, 20):
    for x in range(1, p):
        for y in range(1, p):
            if to10([3,4,x,5], p) + to10([x,9,x,3], p )  == to10([y,y,6,8], p):
                print(p,x,y, to10([y,x,x,y], p))

