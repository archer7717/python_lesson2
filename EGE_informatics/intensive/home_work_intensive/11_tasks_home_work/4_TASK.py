from math import *

for l in range(1, 100000):
    kod = 450+10+26+26
    bit = ceil(log2(kod))

    byte = ceil(bit*l/8)
    if byte*575 > 100*2**10:
        print(l)