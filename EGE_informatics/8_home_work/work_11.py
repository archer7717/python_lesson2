from itertools import product

count = 0

for x in product('ВИШНЯ', repeat=6):
    s = ''.join(x)
    if s.count('В')<=1 and s[0]!='Ш' and s[-1] not in 'ИЯ':
        count+=1
print(count)

