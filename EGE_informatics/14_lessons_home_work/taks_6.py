

x = 11*15**65 + 18*15**38 - 14 * 15**17 + 19 * 15**11 + 18338

s = []
while x > 0:
    s = [x%15] + s 
    x = x //15

q = []

for i in s:
    if i not in q:
        q.append(i)
print(len(q))
