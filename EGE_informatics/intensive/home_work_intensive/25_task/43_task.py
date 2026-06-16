def p(x):
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return [i] + p(x//i)
    return [x]

for x in range(8_000_010, 8_010_000, 100):
    d = p(x)
    if len(d)==len(set(d)):
        print(x, max(d))
