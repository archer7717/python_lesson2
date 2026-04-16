
print('x,y,z,w, F')

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = (x <= z)  and y and (x or w)
                if f == 1:
                    print(x,y,z,w,f)