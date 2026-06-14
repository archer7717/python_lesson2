from itertools import *



B = []

for l in 0,1,2,3,4,5,6:
    for x in product('13579', repeat=l):
        B.append(''.join(x))
m = []
c = []
for a in '02468':
    for b in B:
        x = int(f'1{a}2157{b}4')
        if x > 10**10:
            break
        if x%133 ==0 :
            m.append(x)


for x in sorted(m):
    print(x, x // 133)