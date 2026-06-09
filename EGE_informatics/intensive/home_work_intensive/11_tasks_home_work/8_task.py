from math import *


for l in range(1, 100000):
    kod = 10 + 17
    bit = ceil(log2(kod))
    byte = ceil(l * bit/8)
    if byte*7564230 > 31*2**20:
        print(l)