a = [int(x) for x in open('17-433.txt')]

m = min([x for x in a if 100< abs(x) < 1000 and abs(x)%100==15])
#print(m)


ans = []


for x,y,z in zip(a, a[1:], a[2:]):
    mn = min(x,y,z)
    mx = max(x,y,z)
    if (x>=0 and y>=0 and z>=0 or x<0 and y<0 and z<0) and mn*mx>m**2:
        ans.append(mn*mx)
print(len(ans), min(ans))