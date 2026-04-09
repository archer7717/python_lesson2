from itertools import product

count = 0

for x in product('01234', repeat=6):
    s = ''.join(x)
    if s[-1]!='3' and s[-1]!='4' and s[0] not in '01':
        count+=1
print(count)
