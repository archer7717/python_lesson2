a = [int(x) for x in open('17-3.txt')]

ans = []
for i in range(len(a)-2):
    x,y,z = a[i],a[i+1],a[i+2]
    if abs(x*y*z)%7==0 and abs((x+y+z))%10==5:
        ans.append(x+y+z)
print(len(ans), max(ans))