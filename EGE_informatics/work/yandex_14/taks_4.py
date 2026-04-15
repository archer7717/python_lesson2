


x = 15 * 2401**1500 - 10 * 343**1200 + 40 * 49**1000 - 35 * 7**850 -4805
count = 0
k = []
while x > 0:
    k = [x%49] + k
    x = x // 49
for i in k:
    if i > 9:
        count+=1
print(count)
