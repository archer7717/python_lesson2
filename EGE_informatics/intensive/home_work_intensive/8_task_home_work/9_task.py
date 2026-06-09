from itertools import *

k = 0
a = []
for x in product(sorted('МИЗАНТРОП'), repeat=5):
    s = ''.join(x)
    k+=1
    if k%2==0 and s[0] =='Н' and s.count('Р')==2:
        a.append([k,s])
print(a[-1])