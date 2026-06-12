from EGE_informatics.work.yandex_14.taks_4 import count

a = 17*16**455 + 2 **67 - 4 ** 47 + 58


def to(a):
    s = ''
    while a >0:
        s = str(a%8) + s
        a = a // 8
    return s
count =0

for i in to(a):
    if int(i)==6:
        continue
    if int(i)%2==0:
        count+=1

print(count)