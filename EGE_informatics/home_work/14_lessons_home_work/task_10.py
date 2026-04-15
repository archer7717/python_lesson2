


x = 5* 216**1156 - 4*36**1147 + 6**1153 - 875
s = []
while x > 0:
    s = [x%6] + s
    x = x // 6
print(s.count(5) - s.count(0))
