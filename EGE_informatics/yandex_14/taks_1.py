x = 5**23 + 25**12 - 10

k4 = 0
s = []
while x >0:
    s = [x%5]  + s
    x = x // 5
print(s.count(4))
