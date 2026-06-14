

def p(x):
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return [i] + p(x//i)
    return [x]


for x in range(5_400_000, 5_410_000):
    if len(p(x))>1:
        d = p(x)
        M = max(d) + min(d)
        if M > 60000:
            if str(M) == str(M)[::-1]:
                print(x, M)