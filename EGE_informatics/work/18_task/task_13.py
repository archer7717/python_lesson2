

def f(n):
    if n <=5:
        return n
    if n > 5 and n%5==0:
        return n + f(n/5+1)
    if n > 5 and n%5!=0:
        return n + f(n + 6)
for n in range(1, 500):
    try:
        if f(n)>1000:
            print(n)
    except:
        ...

