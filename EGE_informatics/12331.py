
for n in range(1, 100):
    b = bin(n)[2:]
    if int(b)%2==0:
        b = b + '10'
    else:
        b = "1" +  b +  "01"
    r = int(b, 2)
    if n <=12:
        print(r, n)