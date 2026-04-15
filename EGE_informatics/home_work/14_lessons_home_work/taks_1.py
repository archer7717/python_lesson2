
x = 64**30 + 2 ** 300 - 4

k = 0
s = []
while x > 0:
    s = [x%8] + s
    x = x // 8
print(s.count(7))
