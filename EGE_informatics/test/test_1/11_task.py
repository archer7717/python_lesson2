from math import log2, ceil


n = 257
w = 4080+17
w2 = ceil(log2(w))

end = ceil((257*w2)/8)

print((end* 8388608)/2**20)
