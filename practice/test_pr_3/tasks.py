from jwt.utils import number_to_bytes
from netaddr.strategy.ipv6 import packed_to_int
from pygments.cmdline import main_inner

#1
# a = int(input())
# b = a%100%10
# c = a%100//10
# n = a//100
# print(b+c+n)

#2

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
#     print('YES')
# else:
#     print('NO')

#3
# year = int(input())
# if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
#     print('YES')
# else:
#     print('NO')

#4
# N = int(input())
# i = 1
# while  N>= i**2:
#     print(i**2)
#     i+=1

#5
# N = int(input())
# k = 0
# power = 1
# while power < N:
#     power = power * 2
#     k += 1
#
# print(k)

#6
# count = 0
# while True:
#     numbers = int(input())
#     if numbers == 0:
#         break
#     else:
#         count+=1
# print(count)

#7
# summ = 0
# while True:
#     number = int(input())
#     if number == 0:
#         break
#     else:
#         summ+=number
# print(summ)
#8
# A  = []
# k = 0
# while True:
#     num = int(input())
#     if num == 0:
#         break
#     else:
#         A.append(num)
#
# for x in A:
#     if x%2==0:
#         k+=1
# print(k)

#9
# max = 0
# element = -1
# while element != 0:
#     element = int(input())
#     if element > max:
#         max = element
# print(max)

#10
# k = 0
# max = 0
# elem = -1
# while elem!=0:
#     elem = int(input())
#     if elem > max:
#         max = elem
#         k=1
#     elif max == elem:
#         k +=1
# print(k)
