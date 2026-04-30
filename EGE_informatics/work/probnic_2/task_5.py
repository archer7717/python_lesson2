
def cc(x):
    s = ''
    while x > 0:
        s = str(x%3) + s
        x = x // 3
    return s

summ = 0
for n in range(1, 1000):
    b = cc(n)
    if sum(map(int,b))%2==0:
        b = "2" + b[2:] + "0"
    else:
        b = "20" + b[2:] + "1"

    r = int(b, 3)
    if r > 75:
        print(n, r)