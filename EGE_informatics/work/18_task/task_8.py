
def f(n):
    if n >25:
        return 2*n**3 +1
    if n <=25:
        return f(n+2) + 2*f(n+3)
s = 0
for i in range(1,1000):
    if f(i)%11==0:
        s+=1
print(s)
