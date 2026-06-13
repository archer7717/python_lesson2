for n in range(1, 10000):
    b = bin(n)[2:]
    if b.count('1')%2==0:
        b = b + '0'
    else:
        b = b + '1'
    if b.count('1')%2==0:
        b = b + '0'
    else:
        b = b + '1'

    r = int(b,2)
    #print(r, n)
    if r > 77:
        print(n)

