def p(x):
    for i in range(2, int(x**0.5)+1):
        if x %i==0:
            return [i] + p(x//i)
    return [x]

for x in range(456_789, 459_789):
    d = sorted(set(p(x)))
    if len(d) == 4:
        M = d[0] + d[1] + d[-1] + d[-2]
        if M%114==39:
            print(x, M)
