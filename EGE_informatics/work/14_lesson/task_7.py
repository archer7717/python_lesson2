x = 7**2 + 49**4 - 21

a = []

while x > 0:
    a = [x%14] + a
    x = x //14
print(a.count(10) + a.count(0))
