from itertools import *

count = 0

for x in permutations('ВАЙФУ', r=4):
    s = ''.join(x)
    if s[0]!='Й':
        if not (any(sub in s for sub in ['ВФ','ФВ'])):
            count+=1
            print(s)
print(count)
