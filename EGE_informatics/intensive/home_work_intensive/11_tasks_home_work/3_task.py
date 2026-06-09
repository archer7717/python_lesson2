from math import *

kod = 10 + 1500
bit = ceil(log2(kod))
byte = ceil((bit*163/8))

print(byte*65536/2**10)