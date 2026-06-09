from math import *


for a in range(10**6, 0, -1):
    kod = (26*2+ 10 + a)
    bit = ceil(log2(kod))
    byte = ceil(bit*24/8)
    if byte*5100 <= 170*2**10:
        print(a)