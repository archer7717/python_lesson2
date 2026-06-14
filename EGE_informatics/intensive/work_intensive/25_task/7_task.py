

def div(x):
    b = set()
    for i in range(1, int(x**0.5)+1):
        if x %i==0:
            b.add(i)
            b.add(x//i)
    return sorted(b)
m = []
for x in range(190061, 190073):
    d = [i for i in div(x) if i%2!=0]
    if len(d)==4:
        print(d[-1], d[-2])