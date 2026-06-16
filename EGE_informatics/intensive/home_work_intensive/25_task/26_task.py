def div(x):
    d = set()
    for i in range(2, int((x**0.5))+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(900_001, 901_001):
    d = div(x)
    if len(d)>=2:
        M = d[0] + d[-1]
        if M%100==46:
            print(x , M)
