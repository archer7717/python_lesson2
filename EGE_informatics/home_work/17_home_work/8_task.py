a = [int(x) for x in open('17_1998.txt')]



ans = []
for x,y,z in zip(a[2:], a[1:], a):
    if abs(x*y*z)%7==0 and abs(x+y+z)%10==5:
        ans.append(x+y+z)

print(len(ans), max(ans))