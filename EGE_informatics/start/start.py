

q = 0
for n in range(1, 1000):
    b = bin(n)[2:]
    for k in b:
        q += int(b)
    b = b + str((q%2))
    q = 0
    for k in b:        
        q += int(b)
    b = b + (str(q%2))
    #print(b)
    c = int(b, 2)
    if c < 86:
        print(n, c)

