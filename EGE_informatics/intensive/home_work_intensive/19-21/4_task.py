def f(a, m):
    if a < 222:
        return m%2==0
    if m == 0:
        return 0
    h = [f(a-2, m-1), f(a-5, m-1), f(a//2, m-1)]

    return any(h) if (m-1)%2==0 else all(h)

print('19', [a for a in range(222, 2000) if  f(a, 2) and not  f(a, 1)])

print('20', [a for a in range(222, 2000) if not f(a, 1) and f(a, 3)])
print('21', [a for a in range(222, 2000) if not f(a, 2) and f(a, 4) ])