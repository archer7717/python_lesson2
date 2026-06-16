def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

# for i in range( 1_180_000, 1_200_000):
#     d = div(i)
#     if len(d) >=2:
#         S = d[0] + d[1]
#         if S!=0 and S%2022==0:
#             print(i, S)


for i in range(200_000_001,200_100_001 ):
    d = div(i)
    if len(d) >= 5:
        p = d[0] * d[1] * d[2] * d[3] * d[4]
        if p%10==1 and p <= i:
            print(p, d[4])
