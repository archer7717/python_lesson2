
def f(curr, end):
    if curr > end or curr == 13:
        return 0
    if curr == end:
        return 1
    if curr < end:
        return f(curr+2, end) + f(curr*3, end) + f(curr**2, end)

print(f(3, 49))
