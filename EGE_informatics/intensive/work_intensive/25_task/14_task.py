
def p(x):
    for i in range(2, int(x**0.5)+1):
        if x %i==0:
            return [i] + p(x//i)
    return [x]


for x in range(749_999, 740_000, -1):
    if len(p(x)) > 1:
        d = [i for i in set(p(x)) if i%10==7]
        if len(d)>0:
            F = sum(d)//len(d)
            if F%111==0:
                print(x, F)
