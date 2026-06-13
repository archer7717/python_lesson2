

def fact(x):
    d = []
    i = 2
    while i**2<=x:
        while x%i==0:
            d.append(i)
            x = x // i
        i+=1
    if x >0:
        d.append(x)
    return d

for x in range(5_400_001, 5_450_000):
    d = [i for i in fact(x) if i!=x]
    if len(d)>0:
        M = max(d)+ min(d)
        if M>60000 and str(M)[::-1]==str(M):
            print(x, M)
