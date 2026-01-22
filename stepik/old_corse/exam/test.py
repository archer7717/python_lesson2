# year = int(input())
#
# y_3 = (year % 100)   // 10
# y_4 = (year % 100)   % 10
# if y_3 == 0 and y_4 == 0:
#     print('YES')
# else:
#     print('NO')

# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
#
# if (x1 + y1) % 2 == 0:
#     b = 2
# else:
#     b = 1
# if (x2 + y2) % 2 == 0:
#     b+=2
# else:
#     b+=1
#
# if b == 4 or b == 2:
#     print('YES')
# else:
#     print('NO')

# y = int(input())
# a = input()
#
# if a == 'f' and  10 <= y <= 15:
#     print('Yes')
# else:
#     print('NO')


# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# if abs(x1 - x2) == abs(y1 - y2):
#     print('YES')
# else:
#     print('NO')

# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# if (x1 - x2)*(y1-y2) == 2  or (x1 - x2)*(y1-y2) == -2 :
#     print('YES')
# else:
#     print('NO')


# a = float(input())
# b = float(input())
# S = 1/2 * a * b
# print(type(S))
#
# tf = float(input())
# print((5/9) * (tf-32))
#

a = int(input())
b = int(input())
c = int(input())

d = ((a+b+c)-((max(a,b,c)+min(a,b,c))))
print(min(a,b,c))
print(d)
print(max(a,b,c))


