

def f(s,b , m):
    if s + b >= 154:
        return m%2==0
    if m == 0:
        return 0

    h = [f(s+4, b, m-1), f(s*3, b, m-1), f(s, b+4, m-1), f(s, b*3, m-1 )]
    return any(h) if (m-1)%2==0 else all(h)

print('19)', [s for s in range(1, 143) if f(11, s, 2)]) #16
print('20)', [s for s in range(1, 143) if  not f(11, s, 1) and  f(11, s, 3)])
print('21)', [s for s in range(1, 143) if  not f(11, s, 2) and f(11, s, 4)])
