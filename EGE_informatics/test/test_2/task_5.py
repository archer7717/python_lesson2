

for n in range(6, 100):
    b = bin(n)[2:]
    if n%3==0:
        b = b + b[-3] + b[-2] + b[-1]
    else:
        c = bin((n%3) * 3)[2:]
        b = b + c
    r = int(b, 2)
   # print(r, n)
    if r > 151:
        print(r, n)
