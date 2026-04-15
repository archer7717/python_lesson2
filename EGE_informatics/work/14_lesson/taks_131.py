
mk = 0

for x in range(70000,9,-1):
    a = 5**2025 + 5 **400 - x
    k = 0 
    while a > 0:
        if a%5 ==4:
            k +=1
        a = a // 5
    if k > mk:
        print(k, x)
        mk = k

