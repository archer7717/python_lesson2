
def f(x,y,z):
    return ((z%115==0) and (y%78==0) and (x%51==0)) <= (x*y*z%a==0)


for a in range(1000000, 1, -1):
    if all(f(x,y,z) for x in range(51, 1000, 51) for y in range(78, 10000, 78) for z in range(115, 10000, 115)):
        print(a)
        break
