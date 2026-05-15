def f(n):
    k = 0
    k+=1
    if n >=1:
        k+=1
        k+=f(n-1)
        k+=f(n-3)
        k+=1
    return k
print(f(40))
