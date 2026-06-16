
def f(curr, end, k):
    if curr ==30 or curr==42:
        k+=1
    if curr < end:
        return 0
    if curr == end:
        return k >0
    return f(curr-3, end, k) + f(curr-4, end, k ) + f(curr//2, end, k)

print(f(78,2,0))