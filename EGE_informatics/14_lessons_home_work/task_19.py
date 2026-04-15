

def cc(n, a):
    s = []
    while n > 0:
        s = [n%a] + s
        n = n// a
    return s

k = 0
for i in range(1, 10000000):
    if len(cc(i, 5)) <=4 and len(cc(i, 2)) >= 5 and cc(i, 16)[-1] == 12:
        k+=1
print(k)