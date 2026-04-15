

def cc(x, n):
    s = []
    while x > 0:
        s = [x%n] + s
        x = x // n
    return s





x = 7 * 512**120 - 6*64**100 + 8 **210 - 255

for n in range(8, 100000):
   print(cc(x, n), n)
