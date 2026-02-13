# count = 0
# q = ''
# a = input()
# b = a[::-1]
# # rint(b)
# for c in b:
#     count += 1
#     # print(c, count)
#     if count % 3 == 0:
#         #     print(q, "0")
#         q = q + c + ","
#     # print(q, "1")
#     else:
#         q += c
# print(q)
# q = q[::-1]
# if q[0] == ',':
#     q = q[1:]
#
# print(q)
#
#
# count_1 = 0
# count_2 = 0
# count_3 = 0
# count_4 = 0
# for i in range(int(input())):
#     b = input().split()
#     x, y = int(b[0]), int(b[1])
#     print(x, y)
#     if x > 0:
#     #    print('ДА')
#         if y > 0:
#             count_1 += 1
#         else:
#             count_4 += 1
#     else:
#         if y > 0:
#             count_2 += 1
#         else:
#             count_3 += 1
#
# print(f"Первая четверть:{count_1}",
#       f"Вторая четверть:{count_2}",
#        f"Третья четверть:{count_3}",
#        f"Четвертая четверть:{count_4}",
#        sep='\n'
#       )


# a = input().split()
#
# c = a[0]
# for i in range(len(a) -1):
#     a[i] = a[i+1]
# a[len(a)-1] = c
# print(*a)


#FIXME
# a = input().split()
# c = a[len(a)-1]
# for k in range(len(a)-2, -1, -1):
#     a[k+1] = a[k]
# a[0] = c
# print(*a)



# a = input().split()
# s = []
# for i in range(len(a)):
#     if a[i] not in s:
#         s.append(a[i])
# print(len(s))


#FIXME
# x = []
# flag = False
# for i in range(int(input())):
#     x.append(int(input()))
# q = int(input())
# for i in range(len(x)):
#     for j in range(i+1,len(x)):
#         if x[i] * x[j] == q:
#             flag = True
#             break
#     if flag:
#         break
# if flag:
#     print('ДА')
# else:
#     print("НЕТ")
# x = []
# flag = False
# for i in range(int(input())):
#     x.append(int(input()))
# q = int(input())

#
# a = input()
# b = input()
#
# m = {'камень-камень': 'ничья', 'камень-ножницы': 'Тимур', 'камень-бумага': 'Руслан',
#      'ножницы-ножницы': 'ничья','ножницы-бумага': 'Тимур', 'ножницы-камень': 'Руслан',
#      "бумага-бумага": 'ничья','бумага-камень': 'Тимур','бумага-ножницы': 'Руслан'}
# c = a + "-" + b
# print(m[c])
#
#
# a = input()
# b = input()
#
# m = {'камень-камень': 'ничья', 'камень-ножницы': 'Тимур', 'камень-бумага': 'Руслан',
#         'камень-ящерица': 'Тимур', 'камень-Спок': 'Руслан', 'ножницы-ножницы': 'ничья',
#         'ножницы-бумага': 'Тимур', 'ножницы-камень': 'Руслан', 'ножницы-ящерица': 'Тимур',
#         'ножницы-Спок': 'Руслан', 'бумага-бумага': 'ничья', 'бумага-камень': 'Тимур',
#         'бумага-ножницы': 'Руслан', 'бумага-ящерица': 'Руслан', 'бумага-Спок': 'Руслан',
#         'ящерица-ящерица': 'ничья', 'ящерица-Спок': 'Тимур', 'ящерица-ножницы': 'Руслан',
#         'ящерица-бумага': 'Тимур', 'ящерица-камень': 'Руслан', 'Спок-Спок': 'ничья',
#         'Спок-ножницы': 'Тимур', 'Спок-бамага': 'Руслан', 'Спок-камень': 'Тимур',
#         'Спок-ящерица': 'Руслан'}
#
# c = a + "-" + b
# print(m[c])



# a = input()
# maxx = 0
# count = 0
# for i in range(len(a) -1):
#     if a[i] == a[i + 1] == 'Р':
#         count += 1
#         if count > maxx:
#             maxx = count
#     else:
#         count = 0
#
# if maxx == 0:
#     print(0)
# else:
#     print(maxx +1)

c = []
x = []
for i in range(int(input())):
    x.append(input())
s = ""
for b in x:
    for i in 'антон':
        if i in b:
            c.append(b.index(i))


3 4 5 6 4 0 2 4 6 2 4 9 12 18 9 4 4 0 1 2 1



