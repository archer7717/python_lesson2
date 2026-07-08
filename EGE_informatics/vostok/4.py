
def p(x):
    for i in range(2, int(x**0.5) +1):
        if x %i==0:
            return [i]+p(x//i)

    return [x]

for x in range(7_513_049, 7_600_000):
    d = p(x)
    if len(d) ==2:
        if ('1' in str(d[0]) and '6' in str(d[0]) and   ('1' in str(d[1]) and '6' in str(d[1]))):
            print(x, max(d))