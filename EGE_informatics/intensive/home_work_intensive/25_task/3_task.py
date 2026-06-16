from itertools import *

comb = []
for l in (0,1,2,3):
    for x in product('2468', repeat=l):
        comb.append(''.join(x))
ans = []
for a1 in '0123456789':
    for a2 in comb:
        x = int(f'1592{a2}6{a1}8')
        if x <= 10**10 and x%1996==0:
            ans.append(x)

for i in sorted(ans):
    print(i, i // 1996)