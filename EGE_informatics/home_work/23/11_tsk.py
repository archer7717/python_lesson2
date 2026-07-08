def f(c,e,k):
    if c==22 or c==7: k+=1
    if c<e: return 0
    if c==e: return k!=2
    return f(c//3,e,k)+f(c-3,e,k)

print(f(68,4,0))