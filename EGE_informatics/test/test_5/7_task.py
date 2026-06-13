from itertools import *

k = 0
for x in product('01234789abcdef', repeat=5):
    s = ''.join(x)
    if s[0]!='0':
        s = s.replace('2','0').replace('4','0').replace('6','0').replace('8','0')\
        .replace('a','0').replace('c','0').replace('e','0')
        s = s.replace('3', '1').replace('7', '1').replace('9', '1') \
            .replace('b', '1').replace('d', '1').replace('f', '1')
        if '00' not in s and '11' not in s:
            #print(s)
            k+=1
print(k)