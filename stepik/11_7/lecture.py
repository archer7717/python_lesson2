# zeros = []
# for i in range(10):
#     zeros.append(0)
# print(zeros)

# numbers = []
# for i in range(10):
#     numbers.append(i)
# List  comprehension
# numbers = [i for i in range(10)]
# print(numbers)
#[выражение for переменная in последовательность]

#zeros = [0 for i in range(10)]
#print(zeros)
# squares = [i ** 2 for i in range(10)]
#  print(squares)
# cubes = [i ** 3 for i in range(10, 21)]
# print(cubes)

# chars  = [c for c in 'abcdefg']
# print(chars)
# n = int(input())
# lines = [input() for _ in range(n)]
# print(lines)
# evens = [i for i in range(0, 11) if i%2==0]
# print(evens)

# numbers = [i * j for i in range(1, 5) for j in range(2)]
# print(numbers)

# numbers = []
#
# for i in range(1, 5):
#     for j in range(2):
#         numbers.append(i * j)
# print(numbers)

# animals = ['🐢', '🐈', '🦜', '🐟', '🐍']
# favorite_animals = [animal for animal in animals[1::2]]
#
# print(favorite_animals)
# team = ['Arthur', 'Timur', 'Anton', 'Valera', 'Arthur', 'Sveta']
# lengths = [len(name) for name in team]
#
# print(*lengths)

# food = ['pizza', 'burger', 'sushi', 'salad']
# a =[dish for dish in food if dish[0] == 's']
# print(a)

# a = [number for number in range(100,1001)]
#
# palindromes = [number for number in a if str(number)[::-1] == str(number)]
# print(palindromes)
#a = [int(c)**2 for c in input().split() if str(int(c)**2)[:-1]!='4']

# a = [int(c)**2 for c in input().split() if str(int(c)**2)[:-1]!='4']
#
# a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96,
#      -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71,
#      -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9,
#      -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]
# n = len(a)
#
# for i in range(n):
#     mx = max(a[:n - i])
#     mx_ind = a.index(mx)
#     print(mx)
#     print(mx_ind)
#     a[n - 1 - i], a[mx_ind] = a[mx_ind], a[n - 1 - i]
# print(a)
#
# a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6, 8, -2, 99]
# n = len(a)
#
# for i in range(1, n):
#     elem = a[i]  # берем первый элемент из неотсортированной части списка
#     j = i
#
#     # пока элемент слева существует и больше нашего текущего элемента
#     while j >= 1 and a[j - 1] > elem:
#         # смещаем j-1-й элемент отсортированной части вправо
#         a[j] = a[j - 1]
#         # сами идём влево, дальше ищем место для нашего текущего элемента
#         j -= 1
#
#     # нашли место для нащего текущего элемента из неотсортированной части
#     # и вставляем его на индекс j в отсортированной части
#     a[j] = elem
#
# print('Отсортированный список:', a)