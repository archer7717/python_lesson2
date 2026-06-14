
def fact(x):
    d = []
    i = 2
    while i**2<=x:
        while x%i==0:
            d.append(i)
            x = x // i
        i+=1
    if x >1:
        d.append(x)
    return d

for x in range(6651220,6655220):
    d = fact(x)
    if len(d)==2 and str(d[0]).count('2')==1 and str(d[1]).count('2')==1:
        print(x, max(d))
