x = 2 * 27**7 + 3**10 - 9

s = []

while x > 0:
    s = [x%3] + s
    x = x // 3
print(s.count(0))
