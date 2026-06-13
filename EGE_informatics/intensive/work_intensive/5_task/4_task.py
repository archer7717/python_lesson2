for n in range(1, 1000):
    b = bin(n)[2:]
    summ = 0
    if n%2==0:
        b= b + bin(b.count('1'))[2:]
    else:
        b = '1' + b + '00'

    r = int(b, 2)
    if r > 215:
        print(r, n)

