def f(x,y):
    return (78125!= y + 4*x) or (a> x) and (a >y)

d = []

for x in range(1, 100000):
    y = 78125 - 4*x
    if y > 0:
        d.append([x,y])

print(len(d))


for a in range(1, 100000):
    if all(f(x,y)==1 for x,y in d):
        print(a)
