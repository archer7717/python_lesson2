from itertools import product
count=0
for x in product('AB123',repeat=8):
    s = ''.join(x)
    if s.count('A') + s.count('B') == 2:
        count+=1
print(count)

