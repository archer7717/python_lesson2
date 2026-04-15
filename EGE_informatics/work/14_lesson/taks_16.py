
for x in range(1, 1000):
    a = 64**12 - 8 **14 + x
    s = []
    while a > 0:
        s = [a%8] + s
        a = a //8
    if s.count(7) == 12 and s.count(1) == 1:
        print(x)
