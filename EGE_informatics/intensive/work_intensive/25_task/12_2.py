

def p(x):
    for i in range(2, int(x**0.5) + 1):
        if x %i==0:
            return [i] + p(x//i)

    return [x]

for x in range(25317, 51237):
    d =  sorted(set(p(x)))
    if len(d)>= 6:
        print(x, max(d))
