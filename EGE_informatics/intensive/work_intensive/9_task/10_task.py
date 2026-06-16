b = []
for s in open('9.txt'):
    a = [int(x) for x in s.split()]
    a1 = [x for x in a if a.count(x)==1]
    a3 = [x for x in  a if a.count(x)==3]
    if len(a3)==6 and len(a1)==1 and a1[0] <= min(a3):
        b.append(max(a3))
print(b[-1])