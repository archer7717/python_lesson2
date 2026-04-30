def f(x):
    return ( a%35==0) and ((730%x==0) <= (( a%x!=0) <= (110%x!=0)))
count = 0
for a in range(1, 1001):
    if all(f(x)==1  for x in range(1, 1000000)):
        count+=1
        print(a, count)
