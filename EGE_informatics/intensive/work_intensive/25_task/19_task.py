
def p(x):
    for i in range(2, int(x**0.5) +1):
        if x % i == 0:
            return [i] + p(x//i)
    return [x]

for x in range(89_428_305,90_000_000):
    d = p(x)
    if len(d)>=6 and x%sum(d)==0:
        print(x, sum(d))
