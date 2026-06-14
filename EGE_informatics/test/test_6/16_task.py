from sys import *
setrecursionlimit(123123123)

def f(n):
    if n < 10:
        return 1
    if n >= 10:
        return (n+3) * f(n-3)

print((f(247563)//519 - 477* f(247560))/f(247557))
