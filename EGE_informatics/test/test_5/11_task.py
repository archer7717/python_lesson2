from math import *


for l in range(1,1000):
    kod = 25+487
    bit = ceil(log2(kod))
    byte = ceil(bit*l/8)
    if 516*byte > 170*2**10:
        print(l)