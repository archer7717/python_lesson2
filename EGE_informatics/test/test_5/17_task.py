
a = [int(x) for x in open('17_29840.txt')]

d = len([x for x in a if x<0 and abs(x)%119==0])

m = []
for x,y in zip(a,a[1:]):
    if (x+y) < d:
        m.append(x+y)

print(abs(min(m)), len(m))

