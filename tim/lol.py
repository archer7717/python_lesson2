for x in range(70000, 80000):
    for a in range(2, x // 2):
        if x % a == 0:
            break
    if x % a == 0:
        b = x // a
        M = a + b
        if M % 10 == 8:
            print(x, M, a, b)
