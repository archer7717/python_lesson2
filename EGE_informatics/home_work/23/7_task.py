

def f(curr, end):
    if curr < end or curr==13:
        return 0
    if curr == end:
        return 1
    if curr > end:
        return f(curr-1, end) + f(curr-2, end) + f(curr//3, end)
print(f(19,6)*f(6,4))