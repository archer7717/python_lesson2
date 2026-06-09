from itertools import *

k = 0
a = []

for x in product(sorted('АЛГОРИТМ'), repeat=5):
    s = ''.join(x)
    k+=1
    if k%2==0 and s[0] not in 'АГ' and s.count('Р')>=2:
        print(s, k)