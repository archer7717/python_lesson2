


x = 10*15**65 + 18* 15**38 - 14*15**17 + 19*15**11 + 18388
s = []
a = []
while x > 0:
    s = [x%15] + s
    x = x // 15


for i in s:
    if i not in a :
        a.append(i)
print(a)
print(len(a))


