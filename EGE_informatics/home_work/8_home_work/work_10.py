from itertools import permutations

count = 0

for x in permutations('0234567', r=5):
    s = ''.join(x)
    if s[0]!='0':
        s  = s.replace('5', '3').replace('7','3')
        s = s.replace('2', '0').replace('4', '0').replace('6', '0')
        if '00' not in s and '33' not in s:
            count+=1
print(count)
   
