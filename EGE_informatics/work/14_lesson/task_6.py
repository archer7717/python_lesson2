x = 17**5 + 85**8 - 10
a = []
while x > 0:
    a = [x%17] + a
    x = x//17
print(a.count(16))
