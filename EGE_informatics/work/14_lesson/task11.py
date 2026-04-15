x = 77*81**2031 + 23*729**1037 - 7 * 9**3023


a = []

while x > 0:
    a = [x%81] + a
    x = x // 81
count = 0
for i in a:
    if i%4==0:
        count+=1
print(count)
