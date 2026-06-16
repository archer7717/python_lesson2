
def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for i in range(452022, 462021):
    d = div(i)
    if len(d) > 0:
        M = d[0] + d[-1]
        if M%7==3:
            print(i, M)

