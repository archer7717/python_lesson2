a = [int(x) for x in open('17-435.txt')]


b = min([x for x in a if 100<= abs(x)  <1000 and abs(x)%100==12])
ans = []

for x,y,z in zip(a[2:], a[1:], a):
    if ((x > 0 and y >0 and z >0) or (x <0 and y <0 and z <0)) and min(x,y,z)*max(x,y,z) > b**2:
        ans.append(min(x,y,z)*max(x,y,z))

print(len(ans), min(ans))