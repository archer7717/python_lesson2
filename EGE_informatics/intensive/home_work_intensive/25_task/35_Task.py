

def p(x):
    for i in range(2, int(x**0.5)+1):
        if x %i==0:
            return [i] + p(x//i)
    return [x]

for i in range(749999, 740000, -1):
    d = [x for x in p(i) if x%10==7]
    d = sorted(set(d))
    if len(d)>0:
        F = sum(x for x in d if x%10==7)//len(d)
        if F!=0 and F%111==0:
            print(i, F)