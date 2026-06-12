


def to(a):
    s = ''
    while a >0:
        s = str(a%5) + s
        a = a//5
    return s

for x in range(1, 1000):
    a = 125**200 - 5**x + 74
    if to(a).count('4')==100:
        print(x)