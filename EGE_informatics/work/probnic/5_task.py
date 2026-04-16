

def cc(n):
    s = []
    while n > 0:
        s = [n%5] + s
        n = n // 5
    return s
for x in range( 0, 2501):
    a = 5**85 + 5**7 - x
    c = cc(a)
    if c.count(0) == 80:
        print(x)
