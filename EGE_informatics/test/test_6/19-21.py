def f(a, b, m):
    if a + b >= 154:
        return m%2==0
    if m == 0:
        return 0
    h = [f(a+4, b, m-1), f(a*3, b, m-1),f(a, b+4, m-1),f(a, b*3, m-1)]

    return any(h) if (m-1)%2==0 else all(h)

print('19', [b for b in range(1, 143) if f(11, b, 2)])
print('20', [b for b in range(1, 143) if not f(11, b, 1) and f(11,b,3)])
print('21', [b for b in range(1, 143)  if f(11, b, 4) and not f(11, b, 2)])

