def to_4(n):
    if n == 0:
        return '0'
    s = ''
    while n > 0:
        s = str(n%4) + s
        n = n // 4
    return s

m = []

for n in range(1, 400):
    b = to_4(n)
    if n%3==0:
        b = b[-1] + b[1:-1] + b[0] + '1'
    else:
        b= b + str(n%3)
    r = int(b, 4)
    if r<= 340:
        m.append(r)
print(max(m))
