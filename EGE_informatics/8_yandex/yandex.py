# from itertools import product
#
#
# count = 0
# for x in product('0234567', repeat=5):
#     if x[0] == '0':
#         continue
#     if len(set(x)) != 5:
#         continue
#     for i in range(4):
#         if int(x[i]) % 2 == int(x[i+1]) % 2:
#             break
#     else:
#         count += 1
# print(count)

#
# from itertools import product
#
# count = 0
# for x in product('КАБИНЕТ', repeat=7):
#     s = ''.join(x)
#     if len(set(x)) != 7:
#         continue
#     if not(any( num  in s[-1] for num in ['А','И','Е'])):
#         print(s)
#         count+=1
# print(count)

#
# from itertools import  product
#
# count = 0
#
# for x in product('ВЗГЛЯД', repeat=4):
#     s = ''.join(x)
#     if 1<= s.count('З') <=2:
#         count += 1
#         print(s)
# print(count)


# from itertools import permutations
#
# count = 0
#
# for x in permutations('КОБУРА', r=6):
#     s = ''.join(x)
#     s = s.replace('Б', 'К').replace('Р', 'К')
#     s = s.replace('У', 'О').replace('А', 'О')
#     if s == 'КОКОКО' or s == 'ОКОКОК':
#         count+=1
#
# print(count)

# from itertools import product
#
# count =0
#
# for x in product('ВИШНЯ', repeat=6):
#     s = "".join(x)
#     if s.count('В') <= 1 and s[0] != 'Ш' and s[-1] not in ['И', 'Я']:
#         count += 1
#         print(s)
# print(count)
#


from itertools import product

count = 0

for x in product('0123456789ABCDEF', repeat=5):
    s = ''.join(x)
    if s[0] == "0":
        continue
    count_2 = 0
    for i in s:
        if i in '0123456789':
            count_2 += 1

    if count_2 == 1:   # изменено
        print(s)
        count += 1

print(count)


# from itertools import product
#
# count = 0
#
# for x in product('0234567', repeat=5):
#     s = ''.join(x)
#
#     # Проверка, что все цифры различны
#     if len(set(x)) != 5:
#         continue
#
#     # Проверка первой цифры не 0
#     if x[0] == '0':
#         continue
#
#     # Проверка чередования чётности
#     valid = True
#     for i in range(4):  # только до предпоследней
#         if (int(x[i]) % 2) == (int(x[i + 1]) % 2):  # одинаковая чётность
#             valid = False
#             break
#
#     if valid:
#         count += 1
#
# print(count)


# from itertools import product
#
# count = 0
#
# for x in product('012345', repeat=6):
#




