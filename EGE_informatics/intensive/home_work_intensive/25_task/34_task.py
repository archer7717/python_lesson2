def p(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return [i]+ p(x//i)
    return [x]


for i in range(3_333_338, 3_334_338):
    d = sorted(set(p(i)))
    if len(d)>0:
        R = d[-1] - d[0]
        if R > 1000 and R%3==0:
            print(i, R)