def f(a, b, m):
    if a + b <= 100:
        return m%2==0
    if m == 0:
        return 0
    h = [f(a-3,b-3, m-1), f((a+1)//2, b, m-1), f(a, (b+1)//2, m-1)]

    return any(h) if (m-1)%2==0 else all(h)


print('19' , [b for b in range(53, 100000) if f(48, b, 2)])
print('19' , [b for b in range(53, 100000) if not f(48, b, 1) and f(48, b, 3)])