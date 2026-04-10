from math import ceil,log2

for a in range(1, 10000):
    i = 251
    b = ceil(log2(a))
    w = (i*b)
    w = (w/2**10)
    if w*796 > 171:
        print(a)
