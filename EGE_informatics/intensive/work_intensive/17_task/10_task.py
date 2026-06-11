a = [int(x ) for x in open('17-432.txt')]

mv = sum([x for x in a if x<0])

#print(mv)
ans =[]

for x,y,z in zip(a, a[1:], a[2:]):
    if min(x,y,z)*max(x,y,z) > mv:
        ans.append(x+y+z)

print(len(ans), abs(max(ans)) )
