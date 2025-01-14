b  = 0
n = int(input())
x = []
while n!=0:
    x.append(n)
    n = int(input())
    for i in x:
        if i %2==0 and i>0:
            b +=1
print(b)