
from string import *

def int(s, n):
    s = s[::-1]
    sm = 0
    for i in range(len(s)):
        sm += printable.index(s[i]) * n**i
    return sm

for x in printable[:37]:
    a = int(f'98{x}31', 37) + int(f'1{x}924', 37)
    if a%21==0:
        print(x, a//21)