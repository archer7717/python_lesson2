

def p(x):
    for i in range(2, int((x**0.5))+1):
        if x%i==0:
            return [i]+p(x//i)
    return [x]

for i in range(9_500_001, 9_510_001):
    d = sorted(set(p(i)))
    F = sum(d)//len(d)
    if F!=0 and F%813==0:
        print(i, F)