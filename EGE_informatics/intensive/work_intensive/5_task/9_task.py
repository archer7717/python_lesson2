
def s3(n):
    if n == 0:
        return '0'
    s = ''
    while n > 0:
        s = str(n%3) + s
        n = n//3
    return s
m = []
for n in range(1, 1000):
    b = s3(n)
    if n%3==0:
        b = b + b[-2:]
    else:
        b = b + s3(sum(map(int,b)))
    r = int(b, 3)
    if r%2==0 and r > 220:
        m.append(r  )

print(min(m))

