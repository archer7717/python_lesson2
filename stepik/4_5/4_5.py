# word = int(input())
# if word == 'Python':
#     print('Yes')
# else:
#     print('NO')
from sys import int_info

from pygments.formatters.irc import IRCFormatter

# number = int(input())
# last_number = number %10
# first_number = number//10
#
# if last_number == first_number:
#     print("ДА")
# else:
#     print("НЕТ")
# n_1, n_2, n_3 = int(input()), int(input()), int(input())
# n = 0
# if n_1 % 2 == 0:
#     n+=1
# if n_2 % 2 == 0:
#     n+=1
# if n_3 % 2 == 0:
#     n+=1
# print(n)
# years = int(input())
# if 16 <= 18:
#     print('Доступ разрешен')
# else:
#     print('Доступ разрешен')

# a = int(input())
# b = int(input())
# if a > b:
#     print(b)
# else:
#     print(a)

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
#
# if a < b:
#     min_a_b = a
# else:
#     min_a_b = b
# if  c  < d:
#     min_c_d = c
# else:
#     min_c_d = d

# if min_a_b < min_c_d:
#     min_abcd = min_a_b
# else:
#     min_abcd =  min_c_d
# print(min_abcd)


# a, b, c = int(input()), int(input()), int(input())
# total = 0
# if a > 0:
#     total += a
# if b > 0:
#     total += b
# if c > 0:
#     total += c
# print(total)
#
# num = int(input())
# if  100 <= num <=999:
#     print('YES')
# else:
#     print('NO')

# num = int(input())
# n_1 = num // 100
# n_2 = num % 100 //10
# n_3 = num % 10
# if n_1 != n_3 and n_2 != n_3 and n_2!=n_3 :
#     print('Различны')
# else:
#     print('Одинаковые')


# x = int(input())
# y = int(input())
#
# if x > 0 and y > 0:
#     print('1 четверть')
# if x < 0 and y > 0:
#     print('2 четверть')
# if x < 0 and y < 0:
#     print('3 четверть')
# if x > 0 and y < 0:
#     print('4 четверть')

# n = int(input())
# if  -1 < n < 17:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')
#
# n = int(input())
# if  n  <= -3 or n >= 7:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')

# n = int(input())
# if   -30 < n  <= -2 or 7 < n <= 25:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')

# n = int(input())
#
# if 999 < n <=9999  and (n%7==0 or n%17 == 0):
#     print('YES')
# else:
#     print('NO')

# a, b, c = int(input()), int(input()), int(input())
# if a + b > c and  a + c > b and b + c > a:
#     print('YES')
# else:
#     print("NO")
#
# year = int(input())
# if  year%4==0 and not(year%100==0) or year%400==0:
#     print('YES')
# else:
#     print("NO")


# x1, y1 = int(input()), int(input())
# x2, y2 = int(input()), int(input())
#
# if  y1 == y2 or x1 == x2:
#     print('YES')
# else:
#     print("NO")

# x1, y1 = int(input()), int(input())
# x2, y2 = int(input()), int(input())
#
# if (x1 + 1 == x2 or x2 + 1 == x1 or x1 == x2) and (y1 + 1 == y2 or y2 + 1 == y1 or y1 == y2):
#     print('YES')
# else:
#     print('NO')

x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())

if ( -1 <= x1 - x2 <= 1) and ( -1 <= y1 - y2 <= 1):
    print('YES')
else:
    print('NO')