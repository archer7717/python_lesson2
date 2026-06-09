from itertools import *

k = 0
a = []
for x in product(sorted('МАНГУСТ'), repeat=6):
    s = ''.join(x)
    k+=1
    if s[0]!='У' and s.count('М')==2 and s.count('Г')<=1:
        a.append([k,s])
print(a[-1])