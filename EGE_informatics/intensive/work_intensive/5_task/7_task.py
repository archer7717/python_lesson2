
def cc(n):
    if n == 0:
        return '0'
    s = ''
    while n >0:
        s = str(n%3) + s
        n = n//3
    return s

for n in range(1, 10000):
    b = cc(n)
    if n%3== 0:
        b = '1' + b + '02'
    else:
        b = b + cc(n%3*5)
    r = int(b, 3)

    if r > 177:
        print(n , r)
