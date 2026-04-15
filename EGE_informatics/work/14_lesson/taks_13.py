
for x in range(1, 100):
    a = 81**20 - 9**x + 50
    s = 0
    while a > 0:
        s = s + a%9
        a = a // 9
    if s == 138:
        print(x)
        break

