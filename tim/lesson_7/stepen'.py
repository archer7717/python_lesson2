

# def pow(a:float, n:int):
#     if n == 0:
#         return  1
#     else:
#         return pow(a,n-1) * a


def pow(a:float, n:int):
    if n == 0:
        return  1
    elif n%2 == 1: # нечетные
        return pow(a,n-1) * a
    else: # n чётное
        return pow(a**2,n//2)

print(pow(5,6))