from itertools import *

k = 0
for x in product('0123456789abcdeg', repeat=4):
    s = ''.join(x)
    if s[0] != '0' and s.count('3') == 1:
        # Проверяем, нет ли двух одинаковых символов подряд
        if '00' not in s and '11' not in s and '22' not in s and '33' not in s and \
           '44' not in s and '55' not in s and '66' not in s and '77' not in s and \
           '88' not in s and '99' not in s and 'aa' not in s and 'bb' not in s and \
           'cc' not in s and 'dd' not in s and 'ee' not in s and 'gg' not in s:
            k += 1
print(k)