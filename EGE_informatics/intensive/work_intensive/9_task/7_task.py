k = 0

for s in open('9.txt'):
    a = sorted([int(x) for x in s.split()])
    a1 = [x for x in a if a.count(x)==1]
    a2 = [x for x in a if a.count(x)==2]
    if len(a2) == 2 and len(a1) == 5 \
        and a1[0]*a1[1]*a1[2] > a2[1]**2:
        k+=1
print(k)