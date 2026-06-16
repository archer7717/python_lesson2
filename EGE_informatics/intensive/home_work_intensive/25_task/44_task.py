def p(x):
    for i in range(2, int((x**0.5))+1):
        if x %i==0:
            return [i] + p(x//i)
    return [x]

for i in range(5_000_001,  5_111_001):
    d = [x for x in p(i) if x%100==12]
    d5 = [x for x in d if d.count(x)==5]
    if len(d5)>0:
        print(i, min(d5))