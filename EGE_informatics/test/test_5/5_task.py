
def to3(x):
    if x==0:
        return 0
    s = ''
    while x>0:
        s = str(x%3) + s
        x = x//3
    return s

for n in range(1, 10000):
    b = to3(n)
    if n%3==0:
        b = '12' + b + '0'
    else:
        b = b + to3(n%3*7)
    r = int(b, 3)
    if r >= 798:
        m.append(r)