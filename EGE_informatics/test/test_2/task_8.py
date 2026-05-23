
from itertools import product

k = 0
for x in product('ЕКОФ', repeat=5):
    s = "".join(x)
    #print(s)
    k+=1
    s = s.replace('Ф','К')
    if s.count('О') == 1:
        if 'КО' not in s and 'ОК' not in s:
            print(s, k)
