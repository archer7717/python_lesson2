def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)
for i in range(699_999,650_999 , -1):
    d = div(i)
    if len(d) > 0:
        M = sum(d)//len(d)
        if M%1000==313:
            print(i, M)
