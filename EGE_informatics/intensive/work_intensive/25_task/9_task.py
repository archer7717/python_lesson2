

def div(x):
    b = set()
    for i in range(2, int(x**0.5)+1):
        if x %i==0:
            b.add(i)
            b.add(x//i)
    return sorted(b)

for i in range(500001,510001 ):
    b = [x for x in div(i) if x%10==8 and x!=8]
    if len(b)>0:
        print(i, min(b))
