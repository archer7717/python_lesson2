from itertools import *

k = 0
a = []

for x in product(sorted('ТЕОРИЯ'), repeat=6):
    s = "".join(x)
    k+=1
    if s[0] not in 'РТЯ' and s.count('И')>=2 and k%2!=0:
        a.append([k, s])
print(a[-1])