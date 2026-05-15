cache = {}

def f(n):
    if n not in cache:
        if n == 1:
            cache[n] = 1
        else:
            cache[n]= f(n-1)+3*g(n-1)
    return cache[n]


def g(n):
    if n==1:
        return 1
    return f(n-1) - 2*g(n-1)
s = f(50)

s = str(s)
a = 0

for i in s:
    a +=int(i)

print(a)
