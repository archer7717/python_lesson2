# import random
# number = random.randint(1, 100)
# while True:
#     answer = int(input("Enter a number between 1 and 100: "))
#     if answer == number:
#         print('Вы угадали, поздравляем!')
#         break
#     if answer > number:
#         print('Слишком много, попробуйте еще раз')
#         continue
#     if answer < number:
# #         print('Слишком мало, попробуйте еще раз')
# #         continue
#
# # Чтобы гарантированно угадать задуманное число от 11 до 100100 (включительно) потребуется не более 77 попыток.
# import random
# n = 60
# left = 1
# right = 100
# while True:
#     middle = (left + right) // 2
#     if  middle == n:
#         print('Мы угадали число')
#         print(middle)
#         break
#     if middle < n:
#         left = middle + 1
#         print(middle, right, left, '<')
#         continue
#     if middle > n:
#         right = middle - 1
#         print(middle, right, left, '>')
#         continue
from traceback import print_tb

# import math
# from random import randint
# n = int(input())
# print(math.ceil(math.log2(n+1)))

import random


print('Добро пожаловать в числовую угадайку')
print('Введите число от 1 до 100:')

def is_valid(number):
    if 1 <= int(number) <= 100:
        return True
    else:
        return False
b = random.randint(1, 100)



def is_valid_num():
    while True:
        n = input()
        if is_valid(n):
            return int(n)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')



def comparison():
    while True:
        n =  is_valid_num()
        if n < b:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif  n > b:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!', '\n','Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break



comparison()















