
def f(a,b,c,m):
    if a+ b + c >= 73:
        return m%2==0
    if m == 0:
        return 0
    h = [f(a+3,b,c,m-1),f(a+13,b,c,m-1),f(a+23,b,c,m-1)
        ,f(a,b+3,c,m-1),f(a,b+13,c,m-1),f(a,b+23,c,m-1),f(a,b,c+3,m-1),f(a,b,c+13,m-1),
         f(a, b, c+23, m - 1)
         ]
    return any(h) if (m-1)%2==0 else all(h)

print('19)', [b for b in range(1, 24) if f(2, b, 2*b, 2)])
print('20)', [b for b in range(1, 24) if  not f(2, b, 2*b, 1) and f(2, b, 2*b, 3)])
print('21)', [b for b in range(1, 24) if  not f(2, b, 2*b, 2) and f(2, b, 2*b, 4)])