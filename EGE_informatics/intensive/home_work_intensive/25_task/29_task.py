
def p(x):
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return [i]+p(x//i)
    return [x]

for i in range(32_500_001,  32_501_001):
    d = sorted(set(p(i)))
    S = sum(d)
    if S!=0 and S%145==0:
        print(i, S)
