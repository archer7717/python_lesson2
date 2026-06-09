from math import *

k = 0
for n in range(1, 1_000_000):
    bit = ceil(log2(n))
    num = ceil(312 * bit / 8)
    if 51 * 2 ** 20 < num * 125_700 < 52 * 2 ** 20:
        k += 1
    if num * 125_700 >= 52 * 2 ** 20:
        print(n)
        break

print(k)