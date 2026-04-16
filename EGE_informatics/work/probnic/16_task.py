from sys import *
setrecursionlimit(123412312)

def f(n):
    if n >= 3000:
        return n
    if n < 3000:
        return f(n+1) * n
print((f(52) - 2* f(53))//f(54))