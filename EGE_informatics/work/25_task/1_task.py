


x = 100000123

d = []
for i in range(1, x+1):
    if  x%i==0:
        d.append(i)
print(d)

d = [i for i in range(1, x+1) if x%i==0]
print(d)