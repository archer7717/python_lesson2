


def to10(n, a):
    n = n[::-1]
    s = 0
    for i in range(len(n)):
        s = s + n[i] * a**i
    return s

for x in range(1, 16):
    v =  to10([9,7,5,9, x], 17) + to10([3, x, 1 , 0, 8], 17)
    if (to10([9,7,5,9, x], 17) + to10([3, x, 1 , 0, 8], 17)) % 11 == 0:
        print(x, v//11)