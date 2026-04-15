

def to10(a, n):
    a = a[::-1]
    s = 0
    for i in range(len(a)):
        s = s + a[i] * n**i
    return s


for x in range(57):
    for y in range(57):
        a = to10([5,3,x,6,6,y,3,5], 57)
        if a %56==0 and (y*57 + x)**0.5%1==0:
            print(y*57+x, x*57+y)
