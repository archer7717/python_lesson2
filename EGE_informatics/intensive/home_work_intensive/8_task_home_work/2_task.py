from itertools import *

k = 0
for x in product('01234', repeat=5):
    s = ''.join(x)
    if s[0]!='0' and s.count('0') + s.count('2') + s.count('4') <=3:
        k+=1
print(k)