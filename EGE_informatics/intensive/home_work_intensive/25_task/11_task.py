

def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for i in range(1204300, 1204380):
    d = div(i)
    if len(d) >0:
        s = sum(x for x in d if x%2==0)
        if s!=0 and s%10==0:
            print(i, s)



