from itertools import *
count = 0
for x in product('БАНДЕРОЛЬ', repeat=7):
    s = ''.join(x)
    if s.count('Ь') <= 1:
        s = s.replace('Н', 'Б').replace('Д', 'Б').replace('Р', 'Б').replace('Ь', 'Б').replace('Л','Б')
        if 'ЕБ' not in s and "БЕ" not in s:
            count += 1
            print(s)
print(count)

