from itertools import *

k=0
for x in product('0123456789abcde', repeat=5):
    s = ''.join(x)
    if s[0] != '0' and s.count('8')==1 and  s.count('a') + s.count('b') + s.count('c')+ s.count('d') +s.count('e') >=2:
        print(s)
        k+=1
print(k)