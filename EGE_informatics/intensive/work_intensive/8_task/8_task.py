from itertools import *

k=0
for x in product('0123456', repeat=6):
    s = ''.join(x)
    if s.count('6') ==1 and s[0] !='0':
        s = s.replace('3', '1').replace('5', '1').replace('4', '2').replace('6','2').replace('0', '2')
        if '11' not in s and '22' not in s:
            print(s)
            k+=1
print(k)
