
a = 2**2045 + 2 ** 1800 - 2 ** 1000 + 4**700 - 2024

def to(a):
    s = ''
    while a >0:
        s = str(a%8) + s
        a = a//8
    return s
summ = 0
for a in to(a):
    summ+=int(a)
print(summ)