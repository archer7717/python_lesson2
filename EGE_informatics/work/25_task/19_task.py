
def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)



for i in range(18938, 23145):
    x = i**2
    d = div(x)
    if len(d)==3:
        print(x, max(d))