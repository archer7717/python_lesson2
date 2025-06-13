
A = [0]*100000
i = 0
b = int(input())
maxx = 0
while b != 0:
    A[i] = b
    maxx += A[i]
    i+=1
    b = int(input())
print(round(maxx/i,2))
