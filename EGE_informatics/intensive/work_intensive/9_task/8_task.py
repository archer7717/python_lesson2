k = 0
for s in open('9.txt'):
    a = [int(x) for x in s.split()]
    k+=1
    a1 = [x for x in a if a.count(x)==1]
    a2 = [x for x in a if a.count(x)==2]
    if len(a2)==2 and len(a1)==4 and a2[0] >= sum(a1)/len(a1):
        print(k)
        break