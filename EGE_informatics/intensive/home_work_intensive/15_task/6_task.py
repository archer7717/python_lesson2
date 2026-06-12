
def f(x,y):
    return (x >= 11) or (3 * x< y) or (x * y< a)

for a in range(1, 10000):
    if all(f(x,y)==1 for x in range(1,100) for y in range(1, 100)):
        print(a)