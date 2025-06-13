a = int(input())
b = int(input())
c = int(input())

if max(a,b,c) >= a+b+c-max(a,b,c):
    print('impossible')
else:
    a = a ** 2
    b = b ** 2
    c = c ** 2
    if a+b+c - max(a,b,c) == max(a,b,c):
        print('right')
    elif a+b+c  - max(a,b,c) > max(a,b,c):
        print('acute')
    else:
        print('obtuse')