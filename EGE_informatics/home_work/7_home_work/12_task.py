def tr(n, m, k):
    return n + m > k and n + k > m and m + k > n

def f(x):
    return tr(a, 7, x) <= ((max(x + 5, 14) <= 27) == (not tr(36, 21, x)))

for a in range(1000, 1 , -1):
    if all(f(x) == 1 for x in range(1, 10000)):
        print(a)

