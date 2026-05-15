from itertools import product
k = 0
for x in product('АЕЛПРЬ', repeat=6):
    s = "".join(x)
    #k+=1
    if s.count('П')>=2:
        if s[-1] != 'А' and s[-1] != 'Л':
            k+=1
            print(k,s)
        
