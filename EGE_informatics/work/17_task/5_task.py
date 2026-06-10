a = [int(x) for x in open('17-3.txt')]

#print(len(a))
ans = []
for i in range(len(a)-1):
    x,y = a[i],a[i+1]
 #   c = x*y
    if x*y>0 and (x+y)%7==0:
        ans.append(x*y)
print(len(ans), min(ans))

