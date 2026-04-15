


def cc(a):
    s = []
    while a > 0:
        s = [a % 3] + s
        a = a // 3
    return s

for i in range(20, 31):
    print(cc(i), i)


