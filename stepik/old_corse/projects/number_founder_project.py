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