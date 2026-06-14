from math import *

kod = 17+4080

bit = (ceil(log2(kod)))
byte=(ceil(bit*257/8))

print(8_388_608*byte/2**20)