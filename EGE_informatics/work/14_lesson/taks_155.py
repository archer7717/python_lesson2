s = []
maxx = 0
for x in range(1, 3001):
    a = 4**210 + 4**110 - x
    k4 = 0
    while a >0:
        if a % 4 == 0:
            k4+=1
        a = a // 4
    if k4 >= maxx:
        maxx = k4
        print(maxx, x)
