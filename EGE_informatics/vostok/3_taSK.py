def f(curr, end):
    p = str(curr)
    if curr > end:
        return 0
    if curr==end:
        return 1
    if p[1] < p[2]:
        return f(curr+1, end) + f(int(p[0]+p[2]+p[1]), end)
    else:
        return f(curr+1, end)

print(f(100,150))
