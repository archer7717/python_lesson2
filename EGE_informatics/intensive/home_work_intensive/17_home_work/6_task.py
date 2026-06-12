a = [int(x) for x in open('17_6_1.txt')]


b = max([ x for x in a if 10000<= abs(x) < 100000 and abs(x)%10==3])


ans = []
for x,y,z in zip(a[2:], a[1:], a):
    if (abs(x)%10==3) + (abs(y)%10==3) + (abs(z)%10==3) >=1 \
        and (x+y+z) <= b:
        ans.append(x+y+z)

print(len(ans), max(ans))
