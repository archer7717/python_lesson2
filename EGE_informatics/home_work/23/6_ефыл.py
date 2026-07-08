

def f(curr, end):
    if curr > end or curr==15:
        return 0
    if curr == end:
        return 1
    if curr < end:
        return f(curr + 1, end) + f(curr *2, end)

print(f(2,12)*f(12, 32))