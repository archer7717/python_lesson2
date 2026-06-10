a = [int(x) for x in open('17_1994.txt')]


ans = []
for x,y in zip(a[1:], a):
    if ((x*y)>0) and (x+y)%7==0:
        ans.append(x*y)
print(len(ans), min(ans))
