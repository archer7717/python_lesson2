

def to10(a, n):
    a = a[::-1]
    s = 0
    for i in range(len(a)):
        s = s + a[i] * n**i
    return s
for i in range(1, 1000):
    b = to10(i.split(),3)
    if 20 < b < 30 and b[:-2] == 11:
        print(i)

