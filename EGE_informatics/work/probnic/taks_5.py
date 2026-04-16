
for n  in  range(7, 10000):
    o = oct(n)[2:]
    if int(o)%2 ==0:
        o = o + o[-1]
    else:
        o = o[-1] + o[1:-1] + o[0]

    r = int(o, 8)
    if r < 254:
        print(n, r)