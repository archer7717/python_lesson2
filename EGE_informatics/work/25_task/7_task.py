# def p(x):
#     for i in range(2, int(x**0.5)+1):
#         if x%i==0:
#             return 0
#     return x>1
#
# for i in range(1, 1000):

#факторизация числа
def fact(x):
    d = []
    i = 2
    while i**2 <= x:
        while x%i==0:
            d.append(i)
            x = x // i
        i+=1
    if x >1:
        d.append(x)
    return d
    #если не нужны повторы

for x in range(2, 100):
    print(x,fact(x))