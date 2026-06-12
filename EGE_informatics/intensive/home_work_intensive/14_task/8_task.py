

def to(a):
    s = ''
    while a >0:
        s = str(a%6) + s
        a = a//6
    return s

for x in range(1, 2031):
    a = 6**260 + 6**160 + 6**60 - x
    if to(a).count('0')==202:
        print(x)