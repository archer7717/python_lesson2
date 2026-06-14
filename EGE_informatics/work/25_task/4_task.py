

def div(x):
    d = set()
    for i in range(2, int((x**0.5))+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)











for x in range(1_125_001,1_126_000):
    d = [i for i in div(x) if i%10==7 and i!=7]
    if len(d)>0:
        print(x, min(d))
