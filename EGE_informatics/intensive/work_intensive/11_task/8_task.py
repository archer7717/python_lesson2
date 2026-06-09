from math import *


for a in range(1, 100000):
    bit = ceil(log2(a))
    byte = ceil(bit*172/8)
    if byte * 356984 >= 54*2**20:
        print(a)
        break

