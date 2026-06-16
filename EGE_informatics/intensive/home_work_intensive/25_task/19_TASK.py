def div(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

# for x in range(300_000_001, 300_010_000):
#     d = div(x)
#     if len(d)>=6:
#         print(x, d[-6])
for k in range(1, 10000000000):
    x = 750000 + k
    nk = [i for i in div(x) if i%2==0]
    if len(nk)%2!=0:
        print(k, len(nk))

