

def f(n):
    s = ''
    while n >0:
        s = str(n%3) + s
        n = n //3
    return s


for n in range(1,100):
    b = bin(n)[2:]

    summ = 0
    for i in b:
        summ+=int(i)
    if summ%2==0:
        b = '10' + b[2:] + '0'
    else:
        b = '11' + b[2:] + '1'
    r = int(b,2)

    if r <= 19:
        print(n, r)
