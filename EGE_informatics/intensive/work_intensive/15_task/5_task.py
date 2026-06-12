def f(x):
    return (a%7==0) and ((240%x==0) <= ((a%x!=0 ) <= (780%x!=0)))


dx = [i for i in range(1,10000) if 780%i==0]

for a in range(1, 100000):
    if all(f(x)== 1  for x in dx):
        print(a)