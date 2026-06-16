

def p(x):
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return [i]+p(x//i)
    return [x]

for i in range(55_000_001, 55_100_001 ):

    d = sorted(set(p(i)))
    if len(d) > 0:
        a = [x for x in d if  x%1000==777]
        if len(a) > 0:
            print(i, min(a))
