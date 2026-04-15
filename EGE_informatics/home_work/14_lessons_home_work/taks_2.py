x = 3 * 16**8 - 4**5 + 3


s = []

while x > 0:
    s = [x%4] + s
    x = x // 4

print(s.count(3))

