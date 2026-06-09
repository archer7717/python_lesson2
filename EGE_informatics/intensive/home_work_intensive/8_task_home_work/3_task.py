from itertools import *

k = 0

for x in product('0123456789ab', repeat=6):
    s = ''.join(x)
    if s.count('b') == 1 and s[0]!='0':
        s = s.replace('a', '2').replace('b', '1')
        s = s.replace('2','0').replace('4','0') \
            .replace('6', '0').replace('8','0').replace('3','1') \
            .replace('5', '1').replace('7','1').replace('9', '1')
        if s.count('1') == s.count('0'):
            k+=1
print(k)
