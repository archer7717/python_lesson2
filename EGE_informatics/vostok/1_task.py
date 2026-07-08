from itertools import *

k = 0
for x in product('012345678', repeat=5):
    s = ''.join(x)
    if s[0]!='0':
        if s.count('3')==2:
            for a in '1357':
                s = s.replace(a,'1')
                if '12' not in s and '21' not in s:
                    k+=1
print(k)