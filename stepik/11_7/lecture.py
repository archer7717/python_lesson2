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
evens = [i for i in range(21) if i % 2 == 0]
print(evens)