a = [int(x) for x in open('17_2016.txt')]

ans = []
for i in  a:
    if i%13==7 and i%7!=0 and i%11!=0:
        ans.append(i)
print(len(ans), max(ans)- min(ans))