

def  fact(x):
    d = []
    i = 2
    while i**2<=x:
        while x%i==0:
            d.append(i)
            x = x // i

        i+=1
    if x >1:
        d.append(x)
    return sorted(d)




for i in range(6_700_001, 6_700_400):
    if len(fact(i)) >0:
        s = sum(fact(i))
        if s%2==0 and s%len(fact(i))==0 and s >0:
            print(i, s)