

def fact(x):
    d = []
    i = 2
    while i**2<= x:
        while x%i==0:
            d.append(i)
            x = x // i
        i+=1
    if x >1:
        d.append(x)


    return sorted(set(d))

for x in range(25317, 51238):
    d = fact(x)
    if len(d) >= 6:
        print(x, max(d))

