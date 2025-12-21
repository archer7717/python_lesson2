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
#         print('Слишком мало, попробуйте еще раз')
#         continue

# Чтобы гарантированно угадать задуманное число от 11 до 100100 (включительно) потребуется не более 77 попыток.
import random
left = 1
right = 100
middle = (left + right) // 2
number = random.randint(left, right)
while True:
    if number == middle:
        print('Угадали')
        break
    if middle < number:
        left = middle + 1