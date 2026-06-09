from math import *

for n in range(10**6, 1, -1):
    bit = ceil(log2(33*2 +n))
    num = ceil(bit*21/8)
    if 1300*num <= 25*2**10:
        print(n)