from itertools import permutations
count=0
for x in permutations('ИГРОК'):
    s = ''.join(x)
    if s[0]!='К' and 'РОК' not in s:
        count+=1
print(count)
