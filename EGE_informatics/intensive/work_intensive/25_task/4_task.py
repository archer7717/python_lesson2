# from fnmatch import *
#
# for x in range(10**11, 0, -4013):
#     if fnmatch(str(x), '123?4*5679'):
#         print(x, abs(x//-4013))

from itertools import *

z = []

for l in 0,1,2,3:
    for x in product('0123456789', repeat=l):
        z.append(''.join(x))

print(z)

for a in '0123456789':
    for b in z:
        x = int(f'123{a}4{b}5679')
        if x%4013==0:
            print(x, x // 4013)
       # print(x)