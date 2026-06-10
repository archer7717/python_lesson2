a = [int(x) for x in open('17-5.txt') ]
#print(a)

ans = [int(x) for x in a if (abs(x)%10==5 or abs(x)%10==7) and x%9!=0 and x%11!=0]

print(len(ans), min(ans)+max(ans))