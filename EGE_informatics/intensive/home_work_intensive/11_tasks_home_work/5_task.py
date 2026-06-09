from math import *

for l in range(10**6, 1, -1):
    kod = 10+1234
    bit = ceil(log2(kod))
    byte = ceil(bit*l/8)
    if 65536*byte <= 2050*2**10:
        print(l)