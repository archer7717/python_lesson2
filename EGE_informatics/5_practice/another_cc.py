# def cc(x):
#     s = ''
#     while x > 0:
#         s = str(x%3) + s
#         x = x //3
#     return s
#
# for n in range(1, 1000):
#     b = cc(n)
#     if n%3 == 0:
#         b = "1" + b + "02"
#     else:
#         b =  b + cc((n%3)*4)
#     r = int(b, 3)
#     if r < 199:
#         print(n, r)
from multiprocessing.util import MAXFD

# def cc(x):
#     s = ''
#     while x > 0:
#         s = str(x%7) + s
#         x = x//7
#     return s
# for n in range(1, 100):
#     b = cc(n)
#     if b.count('2')%2==0:
#         b = b + '5' * 3
#     else:
#         b = "1" + b
#     r = int(b, 7)
#     if r < 3799:
#         print(n, r)

# def cc(x):
#     s = ''
#     while x > 0:
#         s = str(x%7) + s
#         x = x//7
#     return s
# for n in range(1, 1000):
#     b = cc(n)
#     if n%7==0:
#         b = b + b[-2] + b[-1]
#     else:
#         b = b + cc((n%7) * 2)
#     r = int(b, 7)
#  #   print(r, n)
#     if r < 220:
#         print(n, r)

# def cc(x):
#     s = ''
#     while x > 0:
#         s = str(x%4) + s
#         x = x//4
#     return s
#
# for n in range(2, 1000):
#     b = cc(n)
#     if n%3 == 0:
#         b = b[-1] + b[1:-1] + b[0]
#         b = b + '1'
#     else:
#         b = b + str(n%3)
#     r = int(b, 4)
#     if r <=340:
# #         print(n, r)
# a = []
# c = 0
# def cc(x):
#     s = ''
#     while x > 0:
#         s = str(x%8) + s
#         x = x//8
#     return s
# for n in range(1, 10000):
#     b = cc(n)
#     if n%2 !=0:
#         b = b + '00'
#     else:
#         b = b + '10'
#     r = int(b, 8)
#     a.append(r)
# for q in a:
#
#     if len(str(q)) == 3:
#         print(q)
#         c+=1
# print(c)
#
# def cc(x):
#     s = ''
#     while x > 0:
#         s = str(x%5) + s
#         x = x//5
#     return s
#
# for n in range(1, 1000):
#     b = cc(n)
#     if sum(map(int, b))%2!=0:
#         #print(b, n)
#         q = b[-1]
#         b = q + b[:-1]
#     else:
#         b = b + cc(n*3)
#     if b.count('0') > 2:
#         print(b, n)
# maxx = 0
# a = '0123456789abcdefg'
#
# def cc(x):
#     s = ''
#     while x > 0:
#         s = a[x % 12] + s
#         x = x // 12
#     return s
#
# for n in range(1, 1000):
#     b = cc(n)
#     if n % 4 == 0:
#         b = '2' + b + '64'
#     else:
#         max_digit = '0'  # Начинаем с минимальной цифры
#         for digit in b:
#             # Ищем максимальную цифру по её позиции в алфавите a
#             if a.index(digit) > a.index(max_digit):
#                 max_digit = digit
#         b = b + max_digit
#     r = int(b, 12)
#     if r > 1799:
#         print(r, n)

# a= []
# for n in range(5,100):
#     b = bin(n)[2:]
#     if n%3==0:
#         b = b + b[-3] + b[-2] + b[-1]
#     else:
#         b = b + bin(((n%3)*3))[2:]
#     r = int(b, 2)
#     if r >151:
#         a.append(r)
#         print(r, n)
# print(min(a))
# q = []
# max = ''
# a = '0123456789abcdefg'
# def cc(x):
#     s = []
#     while x > 0:
#         s.append(a[x%12])
#         x = x//12
#     return s
#
# for n in range(1, 100000):
#    b = cc(n)[::-1]
#
#  #  print(b)
#    if n%4==0:
#        b = "2" + "".join(b) + '64'
#   #     print(b)
#    else:
#        for i in b:
#            if i > max:
#                max = i
#
#        #print(max, n)
#        b = "".join(b) + max
#    r = int(b, 12)
#    if r  > 1799:
#        q.append(r)
# print(min(q))
#


q = []
max = ''
a = '0123456789abcdefg'
def cc(x):
    s = []
    while x > 0:
        s.append(a[x%12])
        x = x//12
    return s

for n in range(10, 100000):
   b = cc(n)[::-1]

   if n%4==0:
       b = "2" + "".join(b) + '64'
   else:
       if 'b' in b:
           b = "".join(b) + 'b'
       elif 'a' in b:
           b = "".join(b)  + 'a'
       else:
           c  = [int(i) for i in b]
           c.sort()
          # print(c)
           b = "".join(b) + str(c[-1])
   r = int(b, 12)
   if r > 1799:
       q.append(r)
print(min(q))


























