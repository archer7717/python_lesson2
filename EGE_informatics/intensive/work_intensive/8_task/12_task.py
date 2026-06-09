from itertools import *
k = 0
for x in product(sorted('СОЛНЦЕ'), repeat=5):
    s = ''.join(x)
    k+=1
   # print(k,s)
    if s.count('Е') <= 1 and 'Л' not in s:
        print(k, s)
   # input()