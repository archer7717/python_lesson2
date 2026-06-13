m = []
for n in range(1, 1000):
    b = bin(n)[2:]
    if n%2==0:
        b = '10' + b + '0'
    else:
        b = '1' + b + "10"
    r = int(b, 2)
    if r > 320:
        m.append(r)

print(min(m))