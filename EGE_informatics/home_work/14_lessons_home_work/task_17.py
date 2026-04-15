

def f(x, cc):
    a = []
    while x > 0:
        a = [x%cc] + a
        x = x // cc
    return a

for n in range(2, 20):
    print(n  , f(68,n))

