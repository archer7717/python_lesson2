from itertools import *

zep = [''.join(x) for x in product('01',repeat=8)]

p = {x for x in zep if x[0] + x[1] == '11'}
q = {x for x in zep if x[-1]=='0'}
a = set()

def f(x):
    P = x in p
    Q = x in q
    A = x in a
    return (not A) <= (P or (not Q))

for x in zep:
    if f(x) == 0:
        a.add(x)
print(len(a))

