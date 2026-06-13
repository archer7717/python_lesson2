
def to_3(n):
    if n == 0:
        return '0'
    s = ''
    while n > 0:
        s = str(n%3) + s
        n = n//3
    return s

for n in range(1, 100000):
    b = to_3(n)
    if n%5==0:
        b = b + b[-3:]
    else:
        b = b + to_3((n%5*5))
    r = int(b, 3)
    if r  < 5496:
        print(n, r)