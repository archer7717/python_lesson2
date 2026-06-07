

def f(s, m):
    if s >= 41:
        return m%2==0
    if m == 0:
        return 0

    if s <= 25:
        h = [f(s + 1, m - 1), f(s + 2, m - 1),  f(s*2, m - 1)]
    else:
        h = [f(s + 1, m - 1), f(s + 2, m - 1), ]



    return any(h) if (m-1)%2==0 else all(h)

print('19)', [s for s in range(1, 41) if not f(s, 2) and f(s, 4)])

print('20)', [s for s in range(1, 41) if not f(s, 4) and f(s, 6)])

print('21)' ,  [s for s in range(1, 41) if  not f(s, 1) and f(s, 3)])


print('21*)' ,  [s for s in range(1, 41) if  not f(s, 0)  and f(s, 2)] )