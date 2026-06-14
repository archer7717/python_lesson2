

for n in range(1, 1000000):
    b = bin(n)[2:]



    if sum(map(int ,b))%2==0:
        b = '10' + b[2:] + '0'
    else:
        b = '11' + b[2:] + '1'
    r = int(b, 2)
    if r <= 19:
        print(n, r)