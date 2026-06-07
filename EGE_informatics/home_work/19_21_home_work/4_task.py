

def f(a,b , m):
    if a + b >= 77:
        return m%2==0
    if  m == 0:
        return 0

    h = [f(a+1, b, m-1), f(a*2, b, m-1), f(a, b+1, m-1), f(a, b*2, m-1)]

    return any(h) if (m-1)%2==0 else all(h)

print('19)', [b for b in range(1, 70) if f(7,b, 2)])
print('20)', [b for b in range(1, 70) if not f(7, b, 1) and f(7, b, 3)])
print('21)', [b for b in range(1, 70) if not f(7, b, 2) and f(7, b , 4) ])
