

def f(curr, end):
    if curr < end or curr ==29:
        return 0
    if curr == end:
        return 1
    if curr > end:
        return f(curr-4, end) + f(curr//3, end)

print(f(100, 20))


