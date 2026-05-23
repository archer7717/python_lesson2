

def f(m):
    if m >= 2030:
        return m
    if m <2030:
        return m + 2 + f(m+2)
def g(m):
    if m <=2030:
        return m
    if m > 2030:
        return m -2 + g(m-2)

print(g(2100) - f(2100))
