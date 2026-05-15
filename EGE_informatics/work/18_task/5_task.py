def f(n):
    s = 0
    s+=n+1
    if n >1:
        s+=n+5
        s+=f(n-1)
        s+=f(n-2)
    return s
print(f(30))
