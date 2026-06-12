
def f(x,y):
    return (x <a) or (y < a) or (x+2*y > 150)


for a in range(1, 100000):
    if all(f(x,y)==1  for x in range(1000) for y in range(1000) ):
        print(a)