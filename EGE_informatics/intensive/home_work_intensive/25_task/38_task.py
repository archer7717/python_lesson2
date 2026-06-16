

def p(x):
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return [i]+p(x//i)
    return [x]

for i in range(5_700_001,  5_701_001):
    d = sorted(set(p(i)))
    