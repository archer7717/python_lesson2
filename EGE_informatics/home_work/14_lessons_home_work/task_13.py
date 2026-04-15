
def fo10(n, a):
    n = n[::-1]
    s = 0
    for i in range(len(n)):
        s = s + n[i] * a**i
    return s

for x in range(1, 100):
    if fo10([1,3,2],x) + int('13',8) == fo10([1,2,4], x+1):
        print(x)
