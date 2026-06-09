from math import *


kod = 26+ 26 + 10 + 20
bit = ceil(log2(kod))
byte = ceil(bit*25/8) + 30
print(2**20/byte)
