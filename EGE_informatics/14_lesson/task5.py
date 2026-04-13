x = 6**203 + 5*6**405  - 3 * 6**144 + 76

a = []

while x >0:
    a = [x%6] + a
    x = x // 6


print( a.count(0) - a.count(5))

