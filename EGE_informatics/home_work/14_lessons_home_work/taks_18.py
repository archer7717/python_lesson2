


def cc(n,a):
    s = []
    while n > 0:
        s = [n%a] + s
        n = n // a
    return s

for n in range(1, 1000):
    if len(cc(n, 6)) == 2 and len(cc(n, 5)) == 3 and n%11==1:
        print(n)