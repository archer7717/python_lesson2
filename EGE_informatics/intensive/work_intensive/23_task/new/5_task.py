
def f(curr, end):
    if curr > end:
        return 0
    if curr == end:
        return 1
    if curr < end:
        return f(curr+1, end) + f(curr*2, end)

print(f(2,9)*f(9, 20)*f(20, 45))