x = 17 * 125**453 + 117 * 5**231 - 3 * 5**13 - 2357

a = []

while x > 0:
    a = [x%125] + a
    x = x // 125

count = 0
for i in a:
    if i <= 37:
        count+=1
print(count)
