b = int(input())
maxx = 0

while b!=0:
    if b%2==0:
        if maxx < b:
            maxx = b
        maxx = maxx
    else:
        pass
    b = int(input())
print(maxx)