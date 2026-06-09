from math import *

for l in range(1, 10**6):
    kod = 10+52+500
    bit = ceil(log2(kod))
    byte = ceil(l*bit/8)
    if 45877 * byte > 48*2**20:
        print(l)
        break
