def div(x):
    d = set()
    for i in range(2, int((x**0.5))+1):
        if x %i ==0:
            d.add(i)
            d.add(x//i)
    return [1] +sorted(d)

for i in range(769999, 769499, -1):
    d = div(i)
    if len(d) >0:
        A = sum(d)//len(d)
        if A%100==12:
            print(i, A)



