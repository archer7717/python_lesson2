from itertools import *
count = 0
k =0
for x in product(sorted('СОЛНЦЕ'), repeat=6):
    s = ''.join(x)
    k +=1
    if s[0] not in 'ОЕ' and s.count('Ц') == 2 and k%2==0:
        count+=1

        print(s)
print(count)
