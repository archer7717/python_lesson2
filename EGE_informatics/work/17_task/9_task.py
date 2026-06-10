a = [int(x) for x in open('17-282.txt')]

minn = min([int(x) for x in a if x%17==0])


ans = []
#print(min(a))
#print(end_minn)
for x,y in zip(a[1:], a):
    if x%minn==0 or y%minn==0:
        ans.append(x+y)
print(len(ans), max(ans))