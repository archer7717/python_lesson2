def f(x):
    return (a%5==0) and ((2020%a!=0) <=((x%1718==0) <= (2023%a==0)))

for a in range(1, 10000):
    if all(f(x)==1 for x in range(1, 100000)):
        print(a)
