from math import log2, ceil

numbers = 325
a = 16 + 2040

ny = ceil(log2(a))
count = 325* ny # в битах

print((count*8192)/2**20)

