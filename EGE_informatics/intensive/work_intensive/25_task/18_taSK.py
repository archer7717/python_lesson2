


def p(x):
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return [i] + p(x//i)
    return [x]


for x in range(3_600_001, 100000000):
    d = p(x)
    if len(d) ==3 and  '3' in str(d[0]) and '5' in str(d[0]) and \
            '3' in str(d[1]) and '5' in str(d[1]) and '3' in str(d[2]) and '5' in str(d[2]):
        print(x, max(d))

