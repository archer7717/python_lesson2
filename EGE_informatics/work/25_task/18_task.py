

def fact(x):
    d = []
    i = 2
    while i**2<=x:
        while x%i==0:
            d.append(i)
            x = x // i
        i+=1
    if x > 1:
        d.append(x)
    return d

for i in range(24_517_513, 24_617_512):
    d = fact(i)
    if len(d) ==12:
        print(i, max(d))