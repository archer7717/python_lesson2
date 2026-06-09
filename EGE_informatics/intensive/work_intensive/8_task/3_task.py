from itertools import product

k= 0
for x in product('ДГИАШЭ', repeat=5):
    s = ''.join(x)
    if s[0] not in 'ИАЭ' and s[-1] not in 'ДГШ':
        print(s)
        k+=1
print(k)