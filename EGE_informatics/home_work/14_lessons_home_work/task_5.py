


for x in range(1, 1000):
    a = 125**200 - 5**x + 74
    s = []
    while a > 0:
        s = [a%5] + s
        a = a // 5
    if s.count(4) == 100:
        print(x, s)
