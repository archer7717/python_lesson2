from math import log2, ceil

i =252
n = 1710
end = ceil(log2(n))
q = ceil((end * 252)/8)
all1 = (4096*q)/2**10
print(all1)
