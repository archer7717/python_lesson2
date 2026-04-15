x = 625**90 + 125**120 - 5*25

s = []
count = 0

while x > 0:
    s = [x%24] + s
    x = x // 24
for i in s:
    if i %2 == 0:
        count+=1
print(count)
