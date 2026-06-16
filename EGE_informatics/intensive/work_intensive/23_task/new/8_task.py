
def f(curr, end, k):
    if curr == 18 or curr == 30:
        k+=1
    if curr > end  or curr == 28 or curr==36:
        return 0
    if curr==end:
        return k>0
    return f(curr+1, end, k) + f(curr+5, end, k) + f(curr*3, end, k)

print(f(2,49,0))