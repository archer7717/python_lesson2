

a = 6 * 512**180 + 7 * 64**181 + 3 *8**184 + 5 * 8 **125 - 65

count = 0
while a > 0:
    if a%64==0:
        count+=1
    a = a // 64

print(count)