a = [int(x) for x in open('17-4.txt')]
summ = 0
for x in a:
    summ +=x
sr_summ = summ/(len(a))


ans = []

for x,y in zip(a, a[1:]):
    if x < sr_summ and y < sr_summ:
        if int(str((x+y))[-2:]) == 19:
            ans.append(x+y)
print(len(ans), min(ans))

