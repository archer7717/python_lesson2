

def p(x):
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return [i] + p(x//i)
    return [x]

for x in range(1_000_001, 1_001_000):
    d = set(p(x))
    if len(d) == 3:
        print(x, max(d))