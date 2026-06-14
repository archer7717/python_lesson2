
def div(x):
    d = set()
    for i in range(2, int((x*0.5))+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(550000, 560000):
    d = [i for i in div(x) if i%10==7 ]
    if len(d)==3:
        print(x, max(d))
