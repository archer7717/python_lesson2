

def f(a, b, m):
    if a + b >= 68:
        return m%2==0
    if m == 0:
        return 0
    h = [f(a+b,b,m-1),f(a,b+a,m-1),  f(a+1,b,m-1),f(a,b+1,m-1)]

    return any(h) if (m-1)%2==0 else all(h)

print('19)', [b  for b in range(1, 60) if f(8, b, 2)])
print('20)', [b  for b in range(1, 60) if  not f(8, b, 1) and f(8, b, 3)])
print('21)', [b  for b in range(1, 60) if  not f(8, b, 2) and f(8, b, 4)])