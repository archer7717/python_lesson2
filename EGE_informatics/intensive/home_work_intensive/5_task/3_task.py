
m = []
for n in range(1, 10000):
    b = bin(n)[2:]
    if n%5==0:
        b = b + '1'
    else:
        b = b + bin(n%5*2)[2:]
    r = int(b,2)
    if r > 102:
        m.append(r)

print(min(m))