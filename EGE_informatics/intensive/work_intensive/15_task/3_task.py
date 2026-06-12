def f(x):
    return not((x%263==0) <= (x%a==0)) and (x%71==0)

for a in range(1,100000):
    if all(f(x)==0 for x in range(71, 10**6, 71)):
        print(a)