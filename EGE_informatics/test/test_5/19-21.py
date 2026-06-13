def f(s , m):
    if s <= 47:
        return m%2==0
    if m == 0:
        return 0
    h = [f(s-3, m-1), f(s-5, m-1), f((s+1)//2, m-1)]

    return  any(h) if (m-1)%2 == 0 else all(h)

print([s for s in range(48, 10000) if f(s, 2)])
print([s for s in range(48, 10000) if f(s, 3) and not(f(s,1))])

print([s for s in range(48, 10000) if not f(s, 2) and f(s,4)])
#print('19)', [s for s in range(48, 1000000) if game(s, 2)])
