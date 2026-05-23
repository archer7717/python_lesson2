

#a = 27**298 + 27**269 - x

def f(n):
    s = ''
    while n > 0:
        s = str(n%27) + s
        n = n // 27
    return s
maxx = 0
for x in range(1, 7291):
    a = 27**298 + 27**269 - x

    
    if f(a).count('0') > maxx:
         maxx = f(a).count('0')
print(maxx)

