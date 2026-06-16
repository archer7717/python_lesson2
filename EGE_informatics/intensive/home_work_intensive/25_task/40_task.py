def p(x):
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return [i]+p(x//i)
    return [x]

for i in range(1_324_728, 1_325_728):
    d = p(i)
    if len(d) == 2:
        if str(d[0]).count('5') == 1 and  str(d[1]).count('5') == 1:
            print(i, max(d))