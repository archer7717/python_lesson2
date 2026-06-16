def f(curr, end):
    if curr > end or curr==21:
        return 0
    if curr == end:
        return 1
    if curr < end:
        return f(curr*2+1, end) + f(curr+1, end)

print(f(1, 25))