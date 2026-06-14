

def p(x):
    for i in range(2, int(x**0.5)+1):
        if x %i ==0:
            return [i]+p(x//i)
    return [x]

for x in range(700_001, 751_001 ):
    d = p(x)
    if len(d)> 1 and len(set(d))==1:
        print(x, d[0])