

def to10(n, a):
    n = n[::-1]
    s = 0
    for i in range(len(n)):
        s = s + n[i] * a**i
    return s
for x in range(1, 100):
    if to10([1,0,3], x) == to10([9, 7], x+2):
        print(x)
