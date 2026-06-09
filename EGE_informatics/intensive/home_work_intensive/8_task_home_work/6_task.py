from itertools import *

k = 0
for x in product('012345', repeat=6):
    s = ''.join(x)
    if s.count('2')==1 and s[0]!='0':
        s = s.replace('3', '1').replace('5','1')
        if '12' not in s and '21' not in s:
            k += 1
            print(s)
print(k)