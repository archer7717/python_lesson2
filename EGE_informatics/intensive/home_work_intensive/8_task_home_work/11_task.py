from itertools import *

k = 0
a = []

for x in product(sorted('МИНУС'), repeat=4):
    s = ''.join(x)
    k+=1
    s = s.replace('Н', 'М').replace('С', 'М')
    s = s.replace('У', 'И')
    if s.count('М') >= s.count('И'):
        a.append([k,s])

print(a[-1])

