
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
    return sorted(set(d))

for x  in range(250_001, 251_000):
    d = [i for i in fact(x) if i!=x]
    s = sum(d)
    if s!=0 and s%17==0:
        print(x,s)