def to_3(n):
    if n == 0:
        return '0'
    s = ''
    while n > 0:
        s = str(n%3) + s
        n = n//3
    return s
m = []
for n in range(1, 1000):

    b = to_3(n)
    if n%5!=0:
        b = b[:-1] + b[0] + to_3(n%5)
    else:
        b = b + b[-1] *2
    r = int(b, 3)
    if r >123:
        m.append(r)

print(min(m))