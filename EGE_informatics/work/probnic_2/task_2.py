


print('x y z w  ')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = (x and y) or ( (z==y) and w)
                if f == 1:
                    print(x,y,z,w)
print(' ')
print(' ')
print('x y z w  ')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = (x and y) or ( (z==y) and w)
                if f == 0:
                    print(x,y,z,w)