from math import *


for dop in range(1, 10000000):
    kod = 10+26+26+70
    bit = ceil(log2(kod))
    byte = ceil(bit*18/8) + dop
    if 2000* byte <= 100*2**10:
        print(dop)