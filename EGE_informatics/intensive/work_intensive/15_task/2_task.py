


def f(x):
    return (x%a==0) or ((2508 <= x <= 2570) <= ((x%214!=0 ) or (x+a<=5286)))

for a in range(100000, 1, -1):
    if all(f(x)==1 for x in range(2508, 2570)):
        print(a)