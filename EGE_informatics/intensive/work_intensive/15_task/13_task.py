

def f(x,y):
    return (x - 3*y < a) or (y>400) or (x  >56)


for a in range(1, 10000):
    if all(f(x,y)==1  for x in range(1, 57) for y in range(1, 400)):
        print(a)