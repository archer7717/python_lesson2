
def f(curr, end, k):
    if curr == 48 or curr == 61:
        k+=1
    if curr < end:
        return 0
    if curr == end:
        return k==1
    return f(curr-1, end, k) + f(curr//2, end, k) + f(curr//3, end, k)
print(f(106,6,0))