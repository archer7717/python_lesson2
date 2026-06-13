def to(n):
    if n == 0:
        return '0'
    s = ''
    while n > 0:
        s = str(n%3) + s
        n = n//3
    return s

for n in range(1, 1000):
    b = to(n)
    if n%3==0:
        b = b + b[-2] + b[-1]
    else:
        b = b + to(n%3*3)
    r = int(b, 3)

    if r <= 150:
        print(n, r)
