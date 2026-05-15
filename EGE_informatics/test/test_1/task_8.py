from itertools import product
k = 0
for x in product('АЕЛПРЬ', repeat=6):
    s = "".join(x)
    k+=1
    print(k , s)
