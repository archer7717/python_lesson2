

def f(s, b, m):
    if s + b >= 45:
        return m%2==0
    if  m == 0:
        return 0
    h = [f(s+1, b, m-1), f(s*3, b, m-1), f(s, b+1, m-1), f(s,b*3, m-1)]

    return any(h) if (m-1)%2==0 else all(h)

print('19)', [s for s in range(1, 41) if f(4, s, 2)]) #5
print('20)', [s for s in range(1, 41) if f(4, s , 3) and not f(4, s , 1)])
print('21)', [s for s in range(1, 41) if   not f(4, s, 2) and f(4, s, 4)])