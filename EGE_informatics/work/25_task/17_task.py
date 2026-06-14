
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

for x in range(13_475_124,13_599_124 ):
    d = fact(x)
    if len(d)==5 and str(d[0]).count('5') >=1 and  str(d[1]).count('5') >=1 and str(d[2]).count('5') >=1 and str(d[3]).count('5') >=1 \
        and str(d[4]).count('5') >=1:
        print(x, max(d))
