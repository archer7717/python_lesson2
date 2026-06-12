

def to(a):
    s = ''
    while a > 0:
        s = str(a%5) + s
        a = a//5
    return s


for x in range(1, 5556):
    a = 5 ** 150 + 5 ** 135 - x
    if to(a).count('4')==134:
        print(x)