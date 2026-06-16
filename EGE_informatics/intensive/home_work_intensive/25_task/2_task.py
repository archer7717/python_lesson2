from itertools import *



comb = []
for l in 0,1,2,3:

    for b in product('13579', repeat=l):
        comb.append(''.join(b))
ans = []
for a1 in '02468':
    for a2 in comb:
        x = int(f'1{a1}2157{a2}4')
        if x <= 10**10 and x%133==0:
            ans.append(x)
for i in sorted(ans):
    print(i, i // 133)