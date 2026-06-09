from math import *

for kod in range(1, 1000000):
    bit = ceil(log2(kod))
    byte = ceil(bit*80/8)
    if byte*1200 <= 150*2**10:
        print(kod)