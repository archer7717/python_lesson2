from itertools import product

k = 0
for x in product('АЕЛПРЬ',repeat=6):
    s = "".join(x)
    k+=1
    if s[0] == 'Л':
        continue
    if s[0] == 'А':
        continue
    if s.count('П') < 2:
        continue
    
    if k%2!=0:
        print(k, s)
        break


