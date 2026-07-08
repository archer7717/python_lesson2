def f(curr, end, k):
    if curr > end or curr == k :
        return 0
    if curr == end :
        return 1
    if curr < end:
        return f(curr+2, end, k) + f(curr+3, end, k) +f(curr*3, end, k)
print(f(10, 22, 33) * f(22, 49, 33) + f(10, 33, 22) * f(33, 49, 22))