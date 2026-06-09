from itertools import *


k = 0

for x in product('0123456', repeat=6):
    s = ''.join(x)
    if s[0]!= '0' and s.count('6')==1:
        s = s.replace('2','0').replace('4','0').replace('6','0')
        s = s.replace('3', '1').replace('5', '1')
        if '11' not in s and '00' not in s:
            k+=1



print(k)