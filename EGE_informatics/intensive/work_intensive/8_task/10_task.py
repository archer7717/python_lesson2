from itertools import permutations
k = 0
for x in set(permutations('МИМИКРИЯ')):
    s = ''.join(x)
    print(s)
    k+=1
print(k)