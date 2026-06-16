

def p(x):
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return [i]+p(x//i)
    return [x]


for i in range(125697, 125721):
    d = p(i)
    if len(d)==2 and d[0]!=d[1]:
        print(d[0], d[1])
