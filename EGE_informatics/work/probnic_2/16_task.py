from sys import *
setrecursionlimit(1234112312)







def f(n):
    if n <= 1:
        return 1
    if n % 2 == 0 and n > 1:
        return (n//2) * f(n-1)
    else:
        return ((n-1)//2) * f(n-1)
print((f(2024) - f(2022))/f(2021))