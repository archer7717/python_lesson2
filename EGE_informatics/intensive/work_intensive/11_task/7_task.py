from math import *


for l in range(10**6, 1, -1):
    kod = 52+10+458
    bit = ceil(log2(kod))
    byte = ceil(bit * l/8)
    if 862 * byte <= 276*2**10:
        print(l)
        break

