

def f(x,y):
    return (541241!= 5 * x + y) or (a > x) or (a >y)


pair = []

for x in range(1, 200_000):
    y = 541241 - 5 * x
    if y >0:
        pair.append([x,y])

for a in range(90_000, 10_0000):
    if all(f(x,y)== 1 for x,y in pair):
        print(a)
        break