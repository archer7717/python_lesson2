def f(x):
    return (x%a==0) or ((70 <= x <= 80) <= (x%18!=0))
for a in range(100000, 1, -1):
    if all(f(x) == 1 for x in range(1, 100000)):
        print(a)
