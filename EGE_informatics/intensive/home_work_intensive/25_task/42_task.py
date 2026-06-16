def p(x):
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return [i] + p(x//i)
    return [x]

for i in range(3_502_101,3_503_101 ):
    d = p(i)
    if len(d) == 4 and 11 in d:
        print(i, max(d))
