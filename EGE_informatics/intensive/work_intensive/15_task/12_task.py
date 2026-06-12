
def f(x, y):
    return (x<a ) and (y <3*a) or (2*x+y>128)


for a in range(1,10000):
    if all(f(x,y)==1 for x in range(1, 65)for y in range(1, 129)):
        print(a)