def f(a, b):
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a + 2, b) + f(a + 3, b) + f(a + 5, b)


print(f(5, 13) * f(13, 25) - f(5, 13) * f(13, 17) * f(17, 25)
      + f(5, 17) * f(17, 25) - f(5, 13) * f(13, 17) * f(17, 25))