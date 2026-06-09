from math import *

kod = 1020 + 10

byte = ceil(log2(kod))
m = ceil(byte*110/8)
print((32768*m)/2**10)
