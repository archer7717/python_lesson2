
def p(x):
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return [i] + p(x//i)
    return [x]

for i in range(7_305_679,  7_3088_679):
    d = p(i)
    if len(d) == 4 and str(sum(d))== str(sum(d))[::-1]:
        print(i, sum(d))
