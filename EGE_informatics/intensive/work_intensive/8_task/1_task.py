from itertools import product

k = 0



for x in product('ГЕПАРД', repeat=5):
    s = ''.join(x)
    print(s)
    if s.count('Г')== 1 and s[0] !='А' and s[-1] !='Е':
        print(s)
        k += 1


print(k)