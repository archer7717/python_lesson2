from functools import *

@lru_cache(20)
def f(n):
    if n<10: return 1
    return (n+3)*f(n-3)

for i in range(10,247564): f(i)

print((f(247563)//519 - 477*f(247560))/f(247557))