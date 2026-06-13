print('x y z w')

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = (y and not(w) and z) or (y and not(w) and not(x))
                if f == 1:
                    print(x,y,z,w)