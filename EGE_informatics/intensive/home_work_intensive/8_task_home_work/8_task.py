from itertools import *


k = 0
a = []
for x in product(sorted('ПЛЮШКА'), repeat=5):
    s = ''.join(x)
    k+=1
    if s.count('Ю')<=1:
        if 'ШШ' not in s:
            a.append([k,s])

print(a[-1])