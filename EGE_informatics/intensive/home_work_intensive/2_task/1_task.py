print('a b c d')

for a in 0,1:
    for b in 0,1:
        for c in 0,1:
            for d in 0,1:
                f = ((not a) <= b) and (not(b == c)) or (not(c <= d))
                if f == 0:
                    print(a,b,c,d)