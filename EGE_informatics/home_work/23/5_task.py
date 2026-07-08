



def f(a, b):
    if a == b:
        return 1
    if a > b + 1 or a % 3 == 0:
        return 0
    return f(a - 1, b) + f(a * 2, b) + f(a + 3, b)


print(f(5, 28))