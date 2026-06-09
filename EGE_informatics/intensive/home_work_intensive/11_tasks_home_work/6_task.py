from math import *


for kod in range(1, 1000):
    bit = ceil(log2(kod))
    byte = ceil(bit*261/8)
    if 252500 * byte > 31*2**20:
        print(kod)