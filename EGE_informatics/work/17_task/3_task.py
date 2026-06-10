a = [int(x) for x in open('17-5.txt')]
#print(a)

ans = []

for x in a:
    if (int(str(x)[-1]) == 5 or int(str(x)[-1]) == 7) and x%9!=0 and x%11!=0:
        ans.append(x)

print(len(ans), min(ans)+max(ans))