

def p(x):
    for i in range(2, int(x*0.5)+1):
        if x%i==0:
            return [i] + p(x//i)
    return [x]

for x in range(6_651_220,6_661_220 ):
    d = p(x)
    if len(d)==2 and str(d[0]).count('2') and str(d[1]).count('2'):
        print(x, max(d))
