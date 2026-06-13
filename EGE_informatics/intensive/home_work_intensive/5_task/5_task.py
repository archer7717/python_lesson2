
for n in range(1,1000):
    b = bin(n)[2:]
    if n%2==0:
        b = '1' + b + '00'
    else:
        b = '10' +b + '1'
    r = int(b, 2)
    if r < 1000:
        print(n, r)