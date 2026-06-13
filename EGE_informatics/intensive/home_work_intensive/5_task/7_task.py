def to3(n):
    if n == 0:
        return '0'
    s = ''
    while n > 0:
        s = str(n%3) + s
        n = n//3
    return s


for n in range(4, 10000):
    b = to3(n)
    if b[-2:] == '10':
        b = '2' + b
    else:
        b ='1' + b
    r = int(b, 3)
    if r >130:
        print(n, r)