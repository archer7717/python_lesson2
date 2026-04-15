

from string import *


# for x in '0123456789abcdefgh':
#     a = int(f'77968{x}11', 18) + int(f'4{x}213', 18)
#     if a%7 == 0:
#         print(x, a//7)

# for x in '0123456789abcde':
#     a = int(f'97968{x}13', 15) + int(f'7{x}213', 15)
#     if a % 11==0:
#         print(x)


# for x in '0123456789abcdefg':
#     a = int(f'149{x}3', 17) + int(f'{x}612', 17) + int(f'{x}54{x}', 17)
#     if a%7==0:
#         print(x, a // 7)

# for x in printable[:22]:
#     for y in printable[:22]:
#         a = int(f'34256{x}4', 22) + int(f'72847{y}3', 22)
#         if a%125 == 0:
#             print(x, y, a//125)



for x in printable[:14]:
    for y in printable[:14]:
        a = int(f'14{y}5{x}2', 14) + int(f'31{x}2{y}3', 14)
        if a%9==0:
            print(x , y, a//9 , x+y)
