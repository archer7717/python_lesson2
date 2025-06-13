

# def gcd(a,b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)

def gcd(a, b):
    return  a if b == 0 else gcd(b, a%b)