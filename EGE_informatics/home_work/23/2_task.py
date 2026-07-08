def f(curr, end):
    if curr > end:
        return 0
    if curr == end:
        return 1
    if curr < end:
        return f(curr+2,end) + f(curr*3,end)

print(f(6,46)*f(46, 108))