



k_max = []
for x in range(7290, 1, -1):
    a = 27**298 + 27**269 - x
    k = 0
    while a > 0:
        if a%27==0:
            k+=1
        a = a // 27
    k_max.append(k)

print(max(k_max))