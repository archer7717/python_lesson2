


def to10(a, n):
    a = a[::-1]
    s = 0
    for i in range(len(a)):
        s = s + a[i] * n**i
    return s
for x in range(1, 16):
    z = ((to10([1,2,3,x,5], 15)) + (to10([1,x,2,3,3], 15)))
    if ((to10([1,2,3,x,5], 15)) + (to10([1,x,2,3,3], 15))) %14==0:
        print(x, z//14)
