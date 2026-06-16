
def p(x):
    for i in range(2, int((x**0.5))+1):
        if x%i==0:
            return [i]+p(x//i)
    return [x]


for i in range(1_200_001, 1_210_001):
    d = sorted(set(p(i)))
    if len(d) >= 2:
        M = d[0] + d[-1]
        if M > 2000 and M%10==8:
            print(i, M)


