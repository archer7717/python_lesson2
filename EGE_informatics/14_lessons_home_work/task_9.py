
for x in range(1000):
    a = 36**17 - 6 ** x + 71
    s = []
    while a > 0:
        s = [a%6] + s
        a = a // 6
    if sum(s) == 61:
        print(x)
