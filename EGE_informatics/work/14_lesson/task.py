x = 366
a = []

while x>0:
    print(a)
    a = [x%7] + a
    print(a)
    x = x//7
print(a)


