a = [int(x) for x in open('17-4.txt')]

sr_summ = sum(a)/len(a)
ans = []

for x,y in zip(a[1:], a):
    if x < sr_summ and y < sr_summ and (x+y)%100==19:
        ans.append(x+y)
print(len(ans), min(ans))