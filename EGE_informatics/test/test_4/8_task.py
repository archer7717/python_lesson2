from itertools import *
k = 0
for x in product('АБВГД',repeat=3):
    s = ''.join(x)
    k+=1
    print(k,s)
