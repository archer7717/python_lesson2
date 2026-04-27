print('x y z F')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            f = not(x ==( y <= z))
            print(x,y,z,f )
