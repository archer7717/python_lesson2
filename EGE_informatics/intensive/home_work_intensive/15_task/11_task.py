
def f(x):
    return (x%a!=0) <= ((x%28==0) <= (x%49!=0))


for a in range(100000, 0 , -1):
    if all(f(x)==1 for x in range(1,1000000)):
        print(a)