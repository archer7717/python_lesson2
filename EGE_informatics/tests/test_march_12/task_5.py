


for n in range(8,10000):
    b = oct(n)[2:]
    if int(b)%2==0:
        b = b + b[-1]
    else:
        b = b[-1] + b[1:len(b)-1] + b[0]
    r = int(b,8)
    if r < 254:
        print(n,r)
