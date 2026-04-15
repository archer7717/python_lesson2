def to10(n, a):
    n = n[::-1]
    s = 0
    for i in range(len(n)):
        s = s + n[i] * a**i
    return s

for x in range(1, 1000):
    if (to10([3,3,6,4,x ], 11) + to10([x,7,9,4,6], 12)) == to10([5,5,x,8,7], 14):
        print(x, to10([5,5,x,8,7], 14) )