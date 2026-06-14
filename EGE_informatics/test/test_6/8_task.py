from itertools import *
k = 0

for x in product(sorted('АПРЕЛЬ'), repeat=6):
    s = ''.join(x)
    k+=1

    if s[0] not in 'АЛ' and s.count('П')>=2:
        if k%2!=0:
            print(s, k)