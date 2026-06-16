k = 0

for s in open('9.txt'):
    a = [int(x ) for x in s.split()]
    a1= [x for x in a if a.count(x)==1]
    a2 = [x for x in a if a.count(x)==2]
    if len(a2)==2 and  len(a1)==4 and max(a1) + min(a1) <= sum(a2):
        k+=1
print(k)