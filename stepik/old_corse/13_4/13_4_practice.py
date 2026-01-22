# # объявление функции
#
#
# def get_last_index(data, value):
#     count = 0
#     count1 = 0
#     number = data.count(value)
#     if number == 0:
#         return "ERROR!"
#     else:
#         for i in range(len(data)):
#             if data[i] == value:
#                 count += 1
#             if count == number:
#                 return i
#
#
#
# # считываем данные
# data = eval(input())
# value = eval(input())
#
# # вызываем функцию
# print(get_last_index(data, value))



# # объявление функции
# def find_all(target, symbol):
#     b = list()
#     for i in  range(len(target)):
#         if target[i] == symbol:
#             b.append(i)
#     return b
#
# # считываем данные
# s = input()
# char = input()
#
# # вызываем функцию
# print(find_all(s, char))



# объявление функции
# def merge(list1, list2):
#     b = list1 + list2
#     n = len(b)
#     for i in range(n - 1):
#         for j in range(n - 1 - i):
#             if list1[j] > list1[j + 1]:
#                 list1[j], list1[j + 1] = list1[j + 1], list1[j]
#     return b
#
# # считываем данные
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]
#
# # вызываем функцию
# print(merge(numbers1, numbers2))


# def quick_merge(list1, list2):
#     return sorted(list1 + list2)
#
#
#
#
# list1 = []
# for _ in range(int(input())):
#     list2 = [int(input()) for i in input().split()]
#     b = quick_merge(list1, list2)
#
# print(*b)
#















