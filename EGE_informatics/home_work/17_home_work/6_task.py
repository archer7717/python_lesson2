a = [int(x) for x in open('17_1993.txt')]

ans = []

for x,y in zip(a[1:], a):
    if abs(x+y)%3==0 and abs(x+y)%6!=0 and abs(x*y)%10==8:
        ans.append(x+y)

print(len(ans), max(ans))