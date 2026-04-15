
x = 51 * 7**12 - 7**3 - 22
s = []
summ = 0
while x > 0:
    s = [x%7] + s
    x = x // 7

for i in s:
    summ += i
print(summ)
print(sum(s))
