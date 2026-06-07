

def f(a, b, m):
    if a + b >= 45:
        return m%2==0
    if m == 0:
        return 0
    h = [f(a+2, b, m-1), f(a*3, b, m-1),f(a, b+2, m-1),f(a, b*3, m-1), ]

    return any(h) if (m-1)%2 == 0 else all(h)

print('19)', len([(k,s) for k in range(1, 44) for s in range(1, 44) if not f(k, s, 0) and f(k, s, 2)]))
print('20', [s for s in range(1, 44) if  not f(4,s, 1) and f(4, s, 3)])

print('21', [s for s in range(1, 44) if not f(13, s, 2) and f(13, s, 4)])