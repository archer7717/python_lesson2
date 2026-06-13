m = []
for n in range(1, 1000):
    b = bin(n)[2:]

    if n%3==0:
        b = b + '010'
    else:
        b = b + bin(n%3*5)[2:]
    r = int(b, 2)
    if r ==314:
        print(n)