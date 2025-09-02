
n = int(input())

for i in range(1,n+1):
    count = 0
    for b in range(1,i+1):
        if i%b==0:
            count+=1
    print(i,'+'*count, sep='')

