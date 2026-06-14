

def p(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return [i]+ p(x//i)
    return [x]

for x in range(3_333_338, 3_343_337):
    if len(p(x))>1:
        d = p(x)
        R = max(d) - min(d)
        if R > 1000 and R%3==0:
            print(x, R)
