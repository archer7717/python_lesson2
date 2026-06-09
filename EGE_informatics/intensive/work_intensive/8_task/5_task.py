from itertools import product

k =0
for x in product('0123456', repeat=5):
    s = ''.join(x)
    if s[0] in '246' and s[-1] not in '120' and s.count('4') <= 1 and s[0] != '0':
        print(s)
        k+=1
print(k)
