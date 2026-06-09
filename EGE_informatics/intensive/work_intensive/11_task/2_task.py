from math import *

kod = 15
bit = ceil(log2(kod))
byte = ceil(19*bit/8)+36
end = 8192 * byte
print(end/2**10)
