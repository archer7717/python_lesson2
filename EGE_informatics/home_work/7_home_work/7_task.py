def f(x):
    return ((x &673!=0) or (x&189 !=0) ) <= (x&a > 0)

for a in range(1 ,100000):
    if all(f(x)==1 for x in range(1, 10000)):
           print(a)
           break
