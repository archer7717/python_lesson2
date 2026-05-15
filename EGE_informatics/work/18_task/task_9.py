

def f(n):
    if n >30:
        return n**2+3*n+5
    if n <=30 and n%2==0:
        return 2 * f(n+1) + f(n+4)
    if n <= 30 and n%2!=0:
        return f(n+2) + 3 * f(n+5)

s=0
for i in range(1, 1001):
    if str(f(i)).count('0')>=2:
        s+=1
print(s)
