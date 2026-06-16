from fnmatch import fnmatch
from itertools import *

comb = []

for l in 0,1,2:
    for x in product('13579',repeat=l):
        comb.append(''.join(x))
ans = []

for a1 in comb:
    for a2 in '02468':
        for a3 in comb:
            x = int(f'1{a1}2{a2}3{a3}45')
            if x <= 10**8 and x%153==0:
                ans.append(x)

for x in sorted(ans):
    print(x, x//153)

