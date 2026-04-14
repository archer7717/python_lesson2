

def for10(n, a):
    n = n[::-1]
    s = 0
    for i in range(len(n)):
        s = s +  n[i] * a**i
    return s

for x in range(1, 1000):
    if for10([3,3],x+4) - for10([3,3], 4) == 33:
        print(x)
