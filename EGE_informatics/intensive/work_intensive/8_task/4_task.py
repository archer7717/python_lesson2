from itertools import product


k = 0
for x in product('01234', repeat=6):
    s = ''.join(x)
    if s[-1] not in '34' and s[0] != '1' and s[0] != '0':
        print(s)
        k+=1
print(k)
