

def f(x,y):
    return (x*y < a) or (5*x < y) or (486 <= x)


for a in range(1, 10000000):
    if all(f(x,y)== 1 for x  in range(450, 500) for y in range(5*x-50, 5*x+10) ):
        print(a)