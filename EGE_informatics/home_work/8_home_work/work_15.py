from itertools import permutations



count = 0

for x in permutations('ДЕЙКСТРА', r=6):
    s = ''.join(x)
    if any(sub in s for sub in ['ЙД','ЙК','ЙС','ЙТ', 'ЙР']):
           count+=1
           print(s)
print(count)
