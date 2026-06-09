from itertools import *


k  = 0
for x in product('01234567', repeat=5):
    s = ''.join(x)
    s = s.replace('3','1').replace('5','1').replace('7','1')
    if s[0]!='0' and s.count('6') == 1 and '16' not in s and '61' not in s:
        print(s)
        k+=1
print(k)