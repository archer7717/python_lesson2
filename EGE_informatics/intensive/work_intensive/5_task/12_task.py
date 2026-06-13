from glances.outputs.glances_stdout_api_restful_doc import print_top


def to_4(n):
    if n == 0:
        return '0'
    s = ''
    while n > 0:
        s = str(n%3) + s
        n = n // 3
    return s

for n in range(1, 1000):
    b = to_4(n)
    if n%3==0:
        b = '1' + b + b[-2:]
    else:
        b = b + to_4(sum(map(int,b)) * 5)
    r = int(b, 3)
    if 900 <= r <= 1100:
        print(r, n)