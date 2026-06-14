a = [int(x) for x in open('17_29349.txt')]

# Минимальный положительный, кратный 123
b = min(x for x in a if x > 0 and x % 123 == 0)

res = []
for i in range(len(a) - 1):
    s = a[i] + a[i + 1]
    if s < b:
        res.append(s)

